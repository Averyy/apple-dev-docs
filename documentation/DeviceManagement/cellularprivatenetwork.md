# CellularPrivateNetwork

**Framework**: Device Management  
**Kind**: dictionary

The payload to provide device info on private network deployments, including geographical location, preference over Wi-Fi, and network deployment type.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+

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
| User channel | NA |
| Allow manual install | iOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
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

## See Also

- [object Cellular](cellular.md)
  The payload you use to configure cellular settings.
- [object ContentCaching](contentcaching.md)
  The payload you use to configure the content-caching service.
- [object DNSSettings](dnssettings.md)
  The payload you use to configure encrypted DNS settings.
- [object Domains](domains.md)
  The payload you use to configure the domains under an organization’s management.
- [object Firewall](firewall.md)
  The payload you use to configure the firewall.
- [object NetworkUsageRules](networkusagerules.md)
  The payload you use to configure network-usage rules.
- [object Relay](relay.md)
  The payload you use to configure relay settings.
- [object WiFi](wifi.md)
  The payload you use to configure Wi-Fi settings.
- [object WiFiManagedSettings](wifimanagedsettings.md)
  The payload you use to configure managed Wi-Fi settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/cellularprivatenetwork)*