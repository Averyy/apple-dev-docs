# Provisioning Profile List

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of installed provisioning profiles on a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

### Command availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | N/A |
| Requires supervision | N/A |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | AllowProvisioningInspection |

### Example request and response

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
        <string>ProvisioningProfileList</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ProvisioningProfileList</string>
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
    <string>0001_ProvisioningProfileList</string>
    <key>ProvisioningProfileList</key>
    <array>
        <dict>
            <key>ExpiryDate</key>
            <date>2020-02-12T20:58:40Z</date>
            <key>Name</key>
            <string>My Company (February 2019 - February 2020)</string>
            <key>UUID</key>
            <string>493d9dc8-e4c0-4fd8-bd8e-8fd4c0dc7b0c</string>
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
- [object ProvisioningProfileListCommand](./provisioningprofilelistcommand.md)
  The command to get a list of installed provisioning profiles on a device.
- [object ProvisioningProfileListResponse](./provisioningprofilelistresponse.md)
  A response from the device after it processes the command to get a list of installed provisioning profiles on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

**Content-Type**: `application/x-apple-aspen-mdm`  
**Type**: `ProvisioningProfileListCommand`

The request object the server returns for the Provisioning Profile List Command.

## Responses

- `200` OK (`ProvisioningProfileListResponse`, `application/xml`): The response object the system returns for the Provisioning Profile List Command.

## See Also

### Profile management
- [Install Profile](./install-profile-command.md)
  Install a configuration profile on a device.
- [Profile List](./profile-list-command.md)
  Get a list of installed profiles on a device.
- [Remove Profile](./remove-profile-command.md)
  Remove a previously installed profile from the device.
- [Install Provisioning Profile](./install-provisioning-profile-command.md)
  Install a provisioning profile on a device.
- [Remove Provisioning Profile](./remove-provisioning-profile-command.md)
  Remove a previously installed provisioning profile from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/provisioning-profile-list-command)*