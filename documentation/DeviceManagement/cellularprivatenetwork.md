# CellularPrivateNetwork

**Framework**: Device Management  
**Kind**: dictionary

The payload that provides device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
object CellularPrivateNetwork
```

#### Discussion

Specify `com.apple.cellularprivatenetwork.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | N/A |
| Allow manual install | iOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
| Allow multiple payloads | iOS, Shared iPad |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>PayloadContent</key>
	<array>
		<dict>
			<key>CellularDataPreferred</key>
			<true/>
			<key>DataSetName</key>
			<string>ExamplePrivateNetwork</string>
			<key>EnableNRStandalone</key>
			<true/>
			<key>Geofences</key>
			<array>
				<dict>
					<key>Longitude</key>
					<real>-122.009</real>
					<key>Latitude</key>
					<real>37.3346</real>
					<key>Radius</key>
					<real>200</real>
					<key>GeofenceId</key>
					<string>AppleParkGeofence</string>
				</dict>
			</array>
			<key>VersionNumber</key>
			<string>1.0</string>
			<key>PayloadIdentifier</key>
			<string>com.example.cellularprivatenetwork</string>
			<key>PayloadDescription</key>
			<string>GeofenceData</string>
			<key>PayloadType</key>
			<string>com.apple.cellularprivatenetwork.managed</string>
			<key>PayloadUUID</key>
			<string>1d6d6912-708e-441a-9272-526ef05bbe3c</string>
			<key>PayloadVersion</key>
			<integer>1</integer>
		</dict>
	</array>
	<key>PayloadDisplayName</key>
	<string>Cellular Private Network</string>
	<key>PayloadIdentifier</key>
	<string>com.example.myprofile</string>
	<key>PayloadType</key>
	<string>Configuration</string>
	<key>PayloadUUID</key>
	<string>3425E7C2-9B02-49EB-8818-F65AA36DDE83</string>
	<key>PayloadVersion</key>
	<integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object CellularPrivateNetwork.GeofenceItem](cellularprivatenetwork/geofenceitem.md)
  A geofence for a private network.

## Properties

- `CellularDataPreferred` (boolean): Set to `true` to prefer this private network over Wi-Fi.
- `CsgNetworkIdentifier` (string): A string using the 3GPP “CSG_ID” format (defined in 3GPP 23.003, Section 4.7). The device uses this value to match a SIM present on the device. All combinations of `NetworkIdentifier` and `CsgNetworkIdentifier` must be unique across all profiles installed on the device. Available: iOS 18+ | iPadOS 18+
- `DataSetName` (string) *(required)*: The name of the private network configuration data set.
- `EnableNRStandalone` (boolean): Set to `true` if this private network is NR Standalone.
- `Geofences` ([CellularPrivateNetwork.GeofenceItem]): A list of up to 1000 geofences for private networks. Geofencing is only used on iPhone.
- `NetworkIdentifier` (string): A string using the 3GPP “Coordinated NID” (option 1 or option 2) format (defined in 3GPP 31.102, Section 12.7.1). The device uses this value to match a SIM present on the device. All combinations of `NetworkIdentifier` and `CsgNetworkIdentifier` must be unique across all profiles installed on the device. Available: iOS 18+ | iPadOS 18+
- `VersionNumber` (string) *(required)*: The version number of this dataset that the system uses to track updates.

## See Also

- [object Cellular](cellular.md)
  The payload that configures cellular settings.
- [object ContentCachingService](contentcachingservice.md)
  The payload that configures the Content Caching service.
- [object DNSSettings](dnssettings.md)
  The payload that configures encrypted DNS settings.
- [object Domains](domains.md)
  The payload that configures the domains under an organization’s management.
- [object Firewall](firewall.md)
  The payload that configures the firewall.
- [object NetworkUsageRules](networkusagerules.md)
  The payload that configures network-usage rules.
- [object Relay](relay.md)
  The payload that configures relay settings.
- [object WiFi](wifi.md)
  The payload that configures Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload that configures managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/cellularprivatenetwork)*