# Adding Matter support to your ecosystem

**Framework**: MatterSupport

Allow people to add Matter accessories to your platform.

#### Overview

With the MatterSupport framework, you can administer, add, and configure Matter devices in your ecosystem using an iOS device. To onboard a device, you need to configure discovery, set up a home, create an extension request handler, and override its methods.

##### Configure Discovery

Add the following to your app’s `Info.plist` so it can discover Matter-related services. See [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) for more information.

```None
<key>NSBonjourServices</key>
    <array>
        <string>_matter._tcp</string>
        <string>_matterc._udp</string>
        <string>_matterd._udp</string>
</array>
```

##### Set Up the Home

Define the home’s name, then create the topology and pass your ecosystem name and an array of homes.

```swift
import MatterSupport
import os.log

let homes = [MatterAddDeviceRequest.Home(name: "My Home")]
let topology = MatterAddDeviceRequest.Topology(ecosystemName: "MyEcosystemName", homes: homes)
```

Use the newly created topology object to create a request to add a device.

```swift
let request = MatterAddDeviceRequest(topology: topology)
```

You can optionally provide the Matter setup code programmatically while setting up a Matter device in an ecosystem. To do this, pass a string containing the payload information from the device’s packaging, such as a QR code. For more information on when this is appropriate, see [`Matter Allow Setup Payload`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.matter.allow-setup-payload).

```swift
// Provide the Matter setup code programmatically.
let setupCode = "12345678910"
request.setupPayload = MTRSetupPayload(payload: setupCode)

// Provide the Matter setup code programmatically using a QR code and add the MT: prefix.
let qrCodePayload = "MT:12345678910ABCDEFG12"
request.setupPayload = MTRSetupPayload(payload: qrCodePayload)
```

Next, start the user interface flow for adding the device. Handle any errors that may occur during the setup.

```swift
do {
    try await request.perform()
    print("Successfully set up device!")

    // Handle the success full setup request and update your app's UI, register the device in your database, or set up any default automations.
} catch let error as MyMatterAddDeviceExtensionRequestHandler {
    // Handle specific Matter errors.
    switch error {
    case .cancelled:
        print("Someone cancelled the setup process.")
    case .accessDenied:
        print("Access denied - check entitlements and permissions.")
    case .unsupported:
        print("Matter setup is not supported on this device.")
    default:
        print("Failed with Matter error: \(error.localizedDescription).")
    }
} catch {
    // Handle other errors.
    print("Failed to set up device with error: \(error.localizedDescription).")
}
```

##### Create the Extension Request Handler

Subclass [`MatterAddDeviceExtensionRequestHandler`](matteradddeviceextensionrequesthandler.md) and override its methods. This class facilitates the user interface flow during the setup of a new Matter device.

```swift
class MyMatterAddDeviceExtensionRequestHandler: MatterAddDeviceExtensionRequestHandler {
    // Define an error type for pairing failures.
    enum PairingError: Error {
        case invalidCredentials
        case pairingFailed
    }

    // Use OSLog to log debugging information.
    private let logger = Logger(subsystem: "com.yourcompany.matterapp", category: "DeviceSetup")

    override init() {
        super.init()
        logger.debug("MatterAddDeviceExtensionRequestHandler initialized")
    }

    // Override this method to return the rooms in the home.
    override func rooms(in home: MatterAddDeviceRequest.Home?) async -> [MatterAddDeviceRequest.Room] {
        logger.debug("Received request to fetch rooms in home: \(String(describing: home?.name)).")

        // In your app, fetch rooms from your database or ecosystem.
        let rooms: [String] = ["Living Room", "Bedroom", "Office", "Kitchen", "Dining Room"]
        return rooms.map { MatterAddDeviceRequest.Room(displayName: $0) }
    }

    // Override this method to commission the device to your application.
    override func commissionDevice(in home: MatterAddDeviceRequest.Home?, onboardingPayload: String, commissioningID: UUID) async throws {
        logger.debug("Commissioning device in home '\(String(describing: home?.name))' with payload: \(onboardingPayload).")

        do {
            // Parse the onboarding payload and commission the device to your app using the Matter framework APIs.
            logger.info("Successfully commissioned device with ID: \(commissioningID)")

            // Make sure that your application returns from this method when it finished pairing the accessory with your application.
            // Returning from this method indicates to the MatterSupport framework that the pairing process is completed,

            // and the system displays a view to indicate that the pairing process is completed.
        } catch {
            logger.error("Failed to commission device: \(error.localizedDescription)")
            throw PairingError.pairingFailed
        }
    }

    // Override this method to configure the device to your application.
    override func configureDevice(named name: String, in room: MatterAddDeviceRequest.Room?) async {
        logger.debug("Configuring device '\(name)' in room: \(String(describing: room?.displayName))")

        // Retrieve and configure the newly paired device in your ecosystem;
        // for example, find the device, set its name or room, apply default configurations, and save information in your database.
        logger.info("Device '\(name)' successfully configured")
    }

    // Override this method to validate the device's credentials.
    override func validateDeviceCredential(_ deviceCredential: MatterAddDeviceExtensionRequestHandler.DeviceCredential) async throws {
        logger.debug("Validating device credential")

        // This code snippet skips validation for better readability.
        // Make sure to replace the following line with actual validation code.
        let isValid = true

        if !isValid {
            logger.warning("Device credential validation failed")
            throw PairingError.invalidCredentials
        } else {
            logger.info("Device credential successfully validated")
        }
    }

    // Override this method to select a specific Wi-Fi network or to ask the Matter framework to select the default WiFi network.
    override func selectWiFiNetwork(from wifiScanResults: [MatterAddDeviceExtensionRequestHandler.WiFiScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation {
        logger.debug("Selecting WiFi network from \(wifiScanResults.count) scan results")

        // Check if a specific network is available.
        let preferredSSID = "YourPreferredNetwork"
        let preferredNetwork = wifiScanResults.first { result in
            result.ssid == preferredSSID && result.security != .open
        }

        if let network = preferredNetwork {
            // Use stored credentials or prompt the person for their password.
            let credentials = "YourSecurePassword"
            logger.info("Selected specific WiFi network: \(network.ssid)")
            return .network(ssid: network.ssid, credentials: credentials)
        } else {
            // Use the system's default network.
            logger.info("Using default system WiFi network.")
            return .defaultSystemNetwork
        }
    }

    // Override this method to select a specific Thread network or to ask the Matter framework to select the default Thread network.
    override func selectThreadNetwork(from threadScanResults: [MatterAddDeviceExtensionRequestHandler.ThreadScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation {
        logger.debug("Selecting Thread network from \(threadScanResults.count) scan results")

        // Check if a specific network is available by name.
        let preferredNetworkName = "HomeThread"
        let preferredNetwork = threadScanResults.first { result in
            result.networkName == preferredNetworkName
        }

        if let network = preferredNetwork, let extendedPANID = network.extendedPANID {
            logger.info("Selected specific Thread network: \(network.networkName ?? "Unnamed")")
            return .network(extendedPANID: extendedPANID)
        } else {
            // Use the system's default Thread network.
            logger.info("Using default system Thread network")
            return .defaultSystemNetwork
        }
    }
}
```

##### Set the Principal Class

Register the subclass you created above in the app’s `Info.plist` as the [`NSPrincipalClass`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSPrincipalClass) for the `com.apple.matter.support.extension.device-setup` extension point identifier.

```None
<key>NSExtension</key>
<dict>
    <key>NSExtensionPointIdentifier</key>
    <string>com.apple.matter.support.extension.device-setup</string>
    <key>NSExtensionPrincipalClass</key>
    <string>$(PRODUCT_MODULE_NAME).MyMatterAddDeviceExtensionRequestHandler</string>
</dict>
```

## See Also

- [struct MatterAddDeviceRequest](matteradddevicerequest.md)
  A request that adds and sets up a device into an ecosystem.
- [class MatterAddDeviceExtensionRequestHandler](matteradddeviceextensionrequesthandler.md)
  The object that handles configuration and commissioning of a device into an ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/adding-matter-support-to-your-ecosystem)*