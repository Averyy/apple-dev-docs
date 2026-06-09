# Managed Application Attributes

**Framework**: Device Management  
**Kind**: httpRequest

Query attributes in managed apps on a device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

This command allows the server to get attributes of managed apps.

The response doesn’t include apps that Declarative Device Management is managing.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | N/A |
| Requires supervision | N/A |
| Allowed in user enrollment | iOS, visionOS |
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
        <key>Identifiers</key>
        <array>
            <string>com.acme.myenterpriseapp</string>
        </array>
        <key>RequestType</key>
        <string>ManagedApplicationAttributes</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ManagedApplicationAttributes</string>
</dict>
</plist>
```

**Response**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>ApplicationAttributes</key>
    <array>
        <dict>
            <key>Attributes</key>
            <dict>
                <key>VPNUUID</key>
                <string>abcde</string>
            </dict>
            <key>Identifier</key>
            <string>com.acme.myenterpriseapp</string>
        </dict>
    </array>
    <key>CommandUUID</key>
    <string>0001_ManagedApplicationAttributes</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object ManagedApplicationAttributesCommand](managedapplicationattributescommand.md)
  The command to query attributes in managed apps on a device.
- [object ManagedApplicationAttributesResponse](managedapplicationattributesresponse.md)
  A response from the device after it processes the command to query attributes in managed apps on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Managed Application Attributes Command.

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
- [Apply Redemption Code](apply-redemption-code-command.md)
  Complete the installation of an app using a redemption code.
- [Validate Applications](validate-applications-command.md)
  Force validation of developer and universal provisioning profiles for enterprise apps.
- [Managed Application Configuration](managed-application-configuration-command.md)
  Get app configurations from managed apps on a device.
- [Managed Application Feedback](managed-application-feedback-command.md)
  Get app feedback from a managed app on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managed-application-attributes-command)*