# Device Information

**Framework**: Device Management  
**Kind**: httpRequest

Get detailed information about a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

## Mentions

- [Validating a Managed Device Attestation](validating-a-managed-device-attestation-attestation.md)

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Deviceinformation Attestation Hardware Support

The following table indicates which System on Chips (SoCs) support DeviceInformation attestation. Unsupported devices ignore the DevicePropertiesAttestation and DeviceAttestationNonce keys.

| Support status | iPhone, iPad | Mac | Apple TV | Apple Watch | Vision Pro |
| --- | --- | --- | --- | --- | --- |
| Unsupported | A10x Fusion and earlier | Intel | A10x Fusion and earlier | S3 and earlier | none |
| Supported | A11 Bionic and laterAll M series | Apple Silicon | A12 Bionic and later | S4 and later | All |

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | Special Case |

##### Example Request and Response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>Queries</key>
        <array>
            <string>UDID</string>
            <string>Languages</string>
            <string>Locales</string>
            <string>DeviceID</string>
            <string>OrganizationInfo</string>
            <string>LastCloudBackupDate</string>
            <string>AwaitingConfiguration</string>
            <string>MDMOptions</string>
            <string>iTunesStoreAccountIsActive</string>
            <string>iTunesStoreAccountHash</string>
            <string>DeviceName</string>
            <string>OSVersion</string>
            <string>BuildVersion</string>
            <string>ModelName</string>
            <string>Model</string>
            <string>ProductName</string>
            <string>SerialNumber</string>
            <string>DeviceCapacity</string>
            <string>AvailableDeviceCapacity</string>
            <string>BatteryLevel</string>
            <string>CellularTechnology</string>
            <string>ICCID</string>
            <string>BluetoothMAC</string>
            <string>WiFiMAC</string>
            <string>EthernetMACs</string>
            <string>CurrentCarrierNetwork</string>
            <string>SubscriberCarrierNetwork</string>
            <string>CurrentMCC</string>
            <string>CurrentMNC</string>
            <string>SubscriberMCC</string>
            <string>SubscriberMNC</string>
            <string>SIMMCC</string>
            <string>SIMMNC</string>
            <string>SIMCarrierNetwork</string>
            <string>CarrierSettingsVersion</string>
            <string>PhoneNumber</string>
            <string>DataRoamingEnabled</string>
            <string>VoiceRoamingEnabled</string>
            <string>PersonalHotspotEnabled</string>
            <string>IsRoaming</string>
            <string>IMEI</string>
            <string>MEID</string>
            <string>ModemFirmwareVersion</string>
            <string>IsSupervised</string>
            <string>IsDeviceLocatorServiceEnabled</string>
            <string>IsActivationLockEnabled</string>
            <string>IsDoNotDisturbInEffect</string>
            <string>EASDeviceIdentifier</string>
            <string>IsCloudBackupEnabled</string>
            <string>OSUpdateSettings</string>
            <string>LocalHostName</string>
            <string>HostName</string>
            <string>CatalogURL</string>
            <string>IsDefaultCatalog</string>
            <string>PreviousScanDate</string>
            <string>PreviousScanResult</string>
            <string>PerformPeriodicCheck</string>
            <string>AutomaticCheckEnabled</string>
            <string>BackgroundDownloadEnabled</string>
            <string>AutomaticAppInstallationEnabled</string>
            <string>AutomaticOSInstallationEnabled</string>
            <string>AutomaticSecurityUpdatesEnabled</string>
            <string>OSUpdateSettings</string>
            <string>LocalHostName</string>
            <string>HostName</string>
            <string>IsMultiUser</string>
            <string>IsMDMLostModeEnabled</string>
            <string>MaximumResidentUsers</string>
            <string>PushToken</string>
            <string>DiagnosticSubmissionEnabled</string>
            <string>AppAnalyticsEnabled</string>
            <string>IsNetworkTethered</string>
            <string>ServiceSubscriptions</string>
        </array>
        <key>RequestType</key>
        <string>DeviceInformation</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_DeviceInformation</string>
</dict>
</plist>
```

**Response**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CommandUUID</key>
    <string>0001_DeviceInformation</string>
    <key>QueryResponses</key>
    <dict>
        <key>AppAnalyticsEnabled</key>
        <true/>
        <key>AvailableDeviceCapacity</key>
        <real>225.2413330078125</real>
        <key>AwaitingConfiguration</key>
        <false/>
        <key>BatteryLevel</key>
        <real>1.0</real>
        <key>BluetoothMAC</key>
        <string>58:fe:f7:70:9d:9e</string>
        <key>BuildVersion</key>
        <string>17A576</string>
        <key>CarrierSettingsVersion</key>
        <string>38.0</string>
        <key>CellularTechnology</key>
        <integer>3</integer>
        <key>CurrentMCC</key>
        <string>311</string>
        <key>CurrentMNC</key>
        <string>480</string>
        <key>DataRoamingEnabled</key>
        <false/>
        <key>DeviceCapacity</key>
        <real>230.26551818847656</real>
        <key>DeviceName</key>
        <string>iPhone</string>
        <key>DiagnosticSubmissionEnabled</key>
        <true/>
        <key>EASDeviceIdentifier</key>
        <string>V2UVOT7J157L7C1FLLSAABSOV4</string>
        <key>ICCID</key>
        <string>8901 0030 0000 0336 1196</string>
        <key>IMEI</key>
        <string>35 735005 003432 4</string>
        <key>IsActivationLockEnabled</key>
        <false/>
        <key>IsCloudBackupEnabled</key>
        <false/>
        <key>IsDeviceLocatorServiceEnabled</key>
        <false/>
        <key>IsDoNotDisturbInEffect</key>
        <false/>
        <key>IsMDMLostModeEnabled</key>
        <false/>
        <key>IsMultiUser</key>
        <false/>
        <key>IsNetworkTethered</key>
        <false/>
        <key>IsRoaming</key>
        <false/>
        <key>IsSupervised</key>
        <true/>
        <key>MDMOptions</key>
        <dict>
        </dict>
        <key>MEID</key>
        <string>35745019114431</string>
        <key>Model</key>
        <string>993-31388LL</string>
        <key>ModelName</key>
        <string>iPhone</string>
        <key>ModemFirmwareVersion</key>
        <string>2.01.08</string>
        <key>OSVersion</key>
        <string>13.0</string>
        <key>PersonalHotspotEnabled</key>
        <false/>
        <key>PhoneNumber</key>
        <string></string>
        <key>ProductName</key>
        <string>iPhone11,8</string>
        <key>SerialNumber</key>
        <string>C7CX706CKWTK</string>
        <key>ServiceSubscriptions</key>
        <array>
            <dict>
                <key>CarrierSettingsVersion</key>
                <string>41.7.19</string>
                <key>CurrentCarrierNetwork</key>
                <string></string>
                <key>CurrentMCC</key>
                <string>310</string>
                <key>CurrentMNC</key>
                <string>260</string>
                <key>ICCID</key>
                <string>8901 0030 0000 0336 1196</string>
                <key>IMEI</key>
                <string>35 734009 035404 0</string>
                <key>IsDataPreferred</key>
                <true/>
                <key>IsRoaming</key>
                <false/>
                <key>IsVoicePreferred</key>
                <true/>
                <key>Label</key>
                <string>Primary</string>
                <key>LabelID</key>
                <string>EB91134A-B155-4DAB-9D35-CB2EAF82615D</string>
                <key>MEID</key>
                <string>35735009002431</string>
                <key>PhoneNumber</key>
                <string>+12018675309</string>
                <key>Slot</key>
                <string>CTSubscriptionSlotOne</string>
        </dict>
        <dict>
                <key>CarrierSettingsVersion</key>
                <string>41.7.46</string>
                <key>CurrentCarrierNetwork</key>
                <string>AT&amp;T</string>
                <key>CurrentMCC</key>
                <string>310</string>
                <key>CurrentMNC</key>
                <string>410</string>
                <key>EID</key>
                <string>89049032004008882600004821436874</string>
                <key>ICCID</key>
                <string>6905 4911 1205 0650 3488</string>
                <key>IMEI</key>
                <string>35 309418 464558 9</string>
                <key>IsDataPreferred</key>
                <false/>
                <key>IsRoaming</key>
                <false/>
                <key>IsVoicePreferred</key>
                <false/>
                <key>Label</key>
                <string>Secondary</string>
                <key>LabelID</key>
                <string>FDG4225C-L9OY-89BM-JF38-36JR4JOL76B3</string>
                <key>MEID</key>
                <string>35745008005631</string>
                <key>PhoneNumber</key>
                <string>+14152739164</string>
                <key>Slot</key>
                <string>CTSubscriptionSlotTwo</string>
            </dict>
        </array>
        <key>SubscriberCarrierNetwork</key>
        <string>ExampleCarrier</string>
        <key>SubscriberMCC</key>
        <string>001</string>
        <key>SubscriberMNC</key>
        <string>01</string>
        <key>UDID</key>
        <string>00008020-000915083C80012E</string>
        <key>VoiceRoamingEnabled</key>
        <false/>
        <key>WiFiMAC</key>
        <string>58:fe:f5:80:29:f3</string>
        <key>iTunesStoreAccountIsActive</key>
        <false/>
    </dict>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object DeviceInformationCommand](deviceinformationcommand.md)
  The command to get detailed information about a device.
- [object DeviceInformationResponse](deviceinformationresponse.md)
  A response from the device after it processes the command to get detailed information about a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#DeviceInformationCommand`

## Request Body

The request object the server returns for the Device Information Command.

## See Also

- [Device Configured](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [User Configured](user-configured-command.md)
  Inform the device that it can continue past Setup Assistant and finish login.
- [Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/device-information-command)*