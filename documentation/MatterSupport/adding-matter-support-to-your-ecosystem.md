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

let homes = [MatterAddDeviceRequest.Home(name: "My Home")]
let topology = MatterAddDeviceRequest.Topology(ecosystemName: "MyEcosystemName", homes: homes)
```

Use the newly created topology object to create a request to add a device.

```swift
let request = MatterAddDeviceRequest(topology: topology)
```

You can optionally provide the Matter setup code programmatically while setting up a Matter device in an ecosystem. To do this, pass a string containing the payload information from the device’s packaging, such as a QR code. For more information on when this is appropriate, see [`Matter Allow Setup Payload`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.matter.allow-setup-payload).

```swift
let onboardingPayload = "MT:<setup_code>"
let qrCodeParser = MTRQRCodeSetupPayloadParser(base38Representation: onboardingPayload)
request.setupPayload = qrCodeParser.populatePayload()
```

Next, start the user interface flow for adding the device. Handle any errors that may occur during the setup.

```swift
do {
    try await request.perform()
    print("Successfully set up device!")
} catch {
    print("Failed to set up device with error: \(error)")
}
```

##### Create the Extension Request Handler

Subclass [`MatterAddDeviceExtensionRequestHandler`](matteradddeviceextensionrequesthandler.md) and override its methods. This class facilitates the user interface flow during the setup of a new Matter device.

```swift
class MyMatterAddDeviceExtensionRequestHandler: MatterAddDeviceExtensionRequestHandler {
    override init() {
        super.init()
    }

    // Override this method to return the rooms in the home.
    override func rooms(in home: MatterAddDeviceRequest.Home?) async -> [MatterAddDeviceRequest.Room] {
        os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Received request to fetch rooms in home: \(String(describing: home))")

        var rooms: [String] = ["Living Room", "Bedroom", "Office"];
        return rooms.map { MatterAddDeviceRequest.Room(displayName: $0) }
    }

    // Override this method to commission the device.
    override func commissionDevice(in home: MatterAddDeviceRequest.Home?, onboardingPayload: String, commissioningID: UUID) async throws {
        os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Received request to commission device in home \(String(describing: home)) using onboarding payload: \(onboardingPayload) and uuid: \(commissioningID)")

        do {
            // Use Matter framework APIs to pair the accessory to your application with the provided onboardingPayload.            
            os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Successfully paired accessory: \(String(describing: accessory))")
        } catch {
            os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Failed to pair accessory: \(String(describing: error))")
            throw error
        }
    }

    // Override this method to commission the device to your application.
    override func configureDevice(named name: String, in room: MatterAddDeviceRequest.Room?) async {
        os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Received request to configure device with name \(name) in room: \(String(describing: room))")

        // Configure the device with selected attributes.
        let accessory = <Your_Ecosystem_Accessory_Object>
        accessory.name = name
        accessory.roomName = room?.displayName ?? "Room Name Not Available"
    }

    // Override this method to validate the device's credentials.
    override func validateDeviceCredential(_ deviceCredential: MatterAddDeviceExtensionRequestHandler.DeviceCredential) async throws {
        os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Received request to validate device credential: \(String(describing: deviceCredential))")

        // Performs verification and attestation checks.
        var isValid = false

        if !isValid {
            os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Rejecting device credential: \(String(describing: deviceCredential))")
                throw "Failed to validate device credentials"
        } else {
            os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Confirming device credential: \(String(describing: deviceCredential))")
        }
    }

    // Override this method to select a specific Wi-Fi network.
    override func selectWiFiNetwork(from wifiScanResults: [MatterAddDeviceExtensionRequestHandler.WiFiScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.WiFiNetworkAssociation {
        os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Received WiFi scan results: \(String(describing: wifiScanResults))")
        
        // If your application would like to specify a nondefault Wi-Fi network.
        var shouldSelectNetwork = true
        
        if shouldSelectNetwork {
            // Return the SSID and credentials known to your application.
            os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Selecting WiFi network with SSID: \(String(describing: ssid)) Credentials: \(String(describing: credentials))")
            return .network(ssid: ssid, credentials: credentials)
        } else {
            os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Selecting default WiFi network")
            return .defaultSystemNetwork
        }
    }

    // Override this method to select a specific Thread network.
    override func selectThreadNetwork(from threadScanResults: [MatterAddDeviceExtensionRequestHandler.ThreadScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation {
        os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Received Thread scan results: \(String(describing: threadScanResults))")
        
        // If your application would like to specify a nondefault Thread network.
        var shouldSelectNetwork = true
        
        if shouldSelectNetwork {
            // Return `extendedPANID` of the Thread network known to your application.
            os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Selecting Thread network with extendedPANID: \(String(describing: extendedPANID))")
            return .network(extendedPANID: extendedPANID)
        } else {
            os_log_with_type(OS_LOG_DEFAULT, OS_LOG_TYPE_DEBUG,"Selecting default Thread network")
            return .defaultSystemNetwork
        }        
    }
}
```

##### Set the Principal Class

Register the subclass you created above in the app’s `Info.plist` as the [`NSPrincipalClass`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSPrincipalClass) for the `com.apple.matter.support.extension.device-setup` extension point identifier.

## See Also

- [struct MatterAddDeviceRequest](matteradddevicerequest.md)
  A request that adds and sets up a device into an ecosystem.
- [class MatterAddDeviceExtensionRequestHandler](matteradddeviceextensionrequesthandler.md)
  The object that handles configuration and commissioning of a device into an ecosystem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/adding-matter-support-to-your-ecosystem)*