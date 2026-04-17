# Managed Application List

**Framework**: Device Management  
**Kind**: httpRequest

Get the status of all managed apps on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 11.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Mentions

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

#### Discussion

This command returns the status of managed apps from the App Store.

Some statuses are transient and the device removes them after reporting them to the server.

This command doesn’t return apps that Declarative Device Management is managing.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
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
        <key>RequestType</key>
        <string>ManagedApplicationList</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ManagedApplicationList</string>
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
    <string>0080_ManagedApplicationList</string>
    <key>ManagedApplicationList</key>
    <dict>
        <key>com.acme.myenterpriseapp</key>
        <dict>
            <key>ExternalVersionIdentifier</key>
            <integer>0</integer>
            <key>HasConfiguration</key>
            <false/>
            <key>HasFeedback</key>
            <false/>
            <key>IsValidated</key>
            <true/>
            <key>ManagementFlags</key>
            <integer>0</integer>
            <key>Status</key>
            <string>Managed</string>
        </dict>
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
- [object ManagedApplicationListCommand](managedapplicationlistcommand.md)
  The command to get the status of all managed apps on a device.
- [object ManagedApplicationListResponse](managedapplicationlistresponse.md)
  A response from the device after it processes the command to get the status of all managed apps on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#ManagedApplicationListCommand`

## Request Body

The request object the server returns for the Managed Application List Command.

## See Also

- [Install Application](install-application-command.md)
  Install a third-party app on a device.
- [Install Enterprise Application](install-enterprise-application-command.md)
  Install an enterprise app on a device.
- [Installed Application List](installed-application-list-command.md)
  Get a list of the installed apps on a device.
- [Remove Application](remove-application-command.md)
  Remove an app.
- [Apply Redemption Code](apply-redemption-code-command.md)
  Complete the installation of an app using a redemption code.
- [Validate Applications](validate-applications-command.md)
  Force validation of developer and universal provisioning profiles for enterprise apps.
- [Managed Application Attributes](managed-application-attributes-command.md)
  Query attributes in managed apps on a device.
- [Managed Application Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managed-application-list-command)*