# Apply Redemption Code

**Framework**: Device Management  
**Kind**: httpRequest

Complete the installation of an app using a redemption code.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 5.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command provides a redemption code to complete installing an app. Use this when `InstallApplication` returns `NeedsRedemption`, or when `ManagedApplicationList` returns `NeedsRedemption` for the status of the app.

Sending a redemption code to an app that doesn’t need it produces an error.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | NA |
| Required access right | AllowAppInstallation |

##### Example Request and Response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>Identifier</key>
        <string>com.example.app</string>
        <key>RedemptionCode</key>
        <string>SB56LT7YX8RH</string>
        <key>RequestType</key>
        <string>ApplyRedemptionCode</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ApplyRedemptionCode</string>
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
    <string>0001_ApplyRedemptionCode</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-001305842600013A</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object ApplyRedemptionCodeCommand](applyredemptioncodecommand.md)
  The command to complete the installation of an app using a redemption code.
- [object ApplyRedemptionCodeResponse](applyredemptioncoderesponse.md)
  A response from the device after it processes the command to complete the installation of an app using a redemption code.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#ApplyRedemptionCodeCommand`

## Request Body

The request object the server returns for the Apply Redemption Code Command.

## See Also

- [Install Application](install-application-command.md)
  Install a third-party app on a device.
- [Install Enterprise Application](install-enterprise-application-command.md)
  Install an enterprise app on a device.
- [Installed Application List](installed-application-list-command.md)
  Get a list of the installed apps on a device.
- [Managed Application List](managed-application-list-command.md)
  Get the status of all managed apps on a device.
- [Remove Application](remove-application-command.md)
  Remove an app.
- [Validate Applications](validate-applications-command.md)
  Force validation of developer and universal provisioning profiles for enterprise apps.
- [Managed Application Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Managed Application Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apply-redemption-code-command)*