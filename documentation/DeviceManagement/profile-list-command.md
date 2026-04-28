# Profile List

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of installed profiles on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | AllowInspection |

##### Example Request and Response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>ManagedOnly</key>
        <false/>
        <key>RequestType</key>
        <string>ProfileList</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ProfileList</string>
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
    <string>0001_ProfileList</string>
    <key>ProfileList</key>
    <array>
        <dict>
            <key>HasRemovalPasscode</key>
            <false/>
            <key>IsEncrypted</key>
            <false/>
            <key>IsManaged</key>
            <false/>
            <key>PayloadContent</key>
            <array>
                <dict>
                    <key>PayloadDescription</key>
                    <string>Installs a PEM certificate payload.</string>
                    <key>PayloadDisplayName</key>
                    <string>PEM certificate payload</string>
                    <key>PayloadIdentifier</key>
                    <string>com.apple.security.pem.ea74b673-50b9-498c-8314-5cfef174d102</string>
                    <key>PayloadOrganization</key>
                    <string>Acme, Inc.</string>
                    <key>PayloadType</key>
                    <string>com.apple.security.pem</string>
                    <key>PayloadVersion</key>
                    <integer>1</integer>
                </dict>
                <dict>
                    <key>PayloadDescription</key>
                    <string>Enrolls your device into SCEP on this MDM server.</string>
                    <key>PayloadDisplayName</key>
                    <string>MDM SCEP payload</string>
                    <key>PayloadIdentifier</key>
                    <string>com.apple.security.scep.aa48bb57-e657-4a87-b6b0-6f5159055304</string>
                    <key>PayloadOrganization</key>
                    <string>Acme, Inc.</string>
                    <key>PayloadType</key>
                    <string>com.apple.security.scep</string>
                    <key>PayloadVersion</key>
                    <integer>1</integer>
                </dict>
                <dict>
                    <key>PayloadDescription</key>
                    <string>Enrolls your device into this MDM server.</string>
                    <key>PayloadDisplayName</key>
                    <string>MDM</string>
                    <key>PayloadIdentifier</key>
                    <string>com.apple.mdm.4e86d728-2c38-4410-bea2-fbe4b77619e3</string>
                    <key>PayloadOrganization</key>
                    <string>Acme, Inc.</string>
                    <key>PayloadType</key>
                    <string>com.apple.mdm</string>
                    <key>PayloadVersion</key>
                    <integer>1</integer>
                </dict>
            </array>
            <key>PayloadDescription</key>
            <string>Enrolls your device into this MDM server.</string>
            <key>PayloadDisplayName</key>
            <string>Python MDM</string>
            <key>PayloadIdentifier</key>
            <string>com.acme.mdm.mdm</string>
            <key>PayloadOrganization</key>
            <string>Acme, Inc.</string>
            <key>PayloadRemovalDisallowed</key>
            <false/>
            <key>PayloadUUID</key>
            <string>a96f429c-d881-47e7-ad07-eeca163976fb</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object ProfileListCommand](profilelistcommand.md)
  The command to get a list of installed profiles on a device.
- [object ProfileListResponse](profilelistresponse.md)
  A response from the device after it processes the command to get a list of installed profiles on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#ProfileListCommand`

## Request Body

The request object the server returns for the Profile List Command.

## See Also

- [Install Profile](install-profile-command.md)
  Install a configuration profile on a device.
- [Remove Profile](remove-profile-command.md)
  Remove a previously installed profile from the device.
- [Install Provisioning Profile](install-provisioning-profile-command.md)
  Install a provisioning profile on a device.
- [Provisioning Profile List](provisioning-profile-list-command.md)
  Get a list of installed provisioning profiles on a device.
- [Remove Provisioning Profile](remove-provisioning-profile-command.md)
  Remove a previously installed provisioning profile from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/profile-list-command)*