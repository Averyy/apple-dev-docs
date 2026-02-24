# Installed Application List

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of the installed apps on a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Mentions

- [Installing, managing, updating, and removing apps](installing-managing-updating-and-removing-apps.md)

#### Discussion

This command allows the server to query for installed 3rd party applications. The response also includes system apps in macOS, iOS 26 and later, tvOS 26 and later, visionOS 26 and later, and watchOS 26 and later.

This command doesn’t return apps that Declarative Device Management is managing if the `ManagedAppsOnly` key is set to `true`, or if the enrollment type is a user enrollment.

Refer to the following sections to determine supported channels and requirements, and to see request and response examples for iOS and macOS.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS |
| Requires supervision | macOS |
| Allowed in user enrollment | iOS, visionOS |
| Required access right | AllowQueryApplications |

##### Example Request and Response

**Managed**:

This command lists only managed apps.

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>ManagedAppsOnly</key>
        <true/>
        <key>RequestType</key>
        <string>InstalledApplicationList</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_InstalledApplicationList</string>
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
    <string>0001_InstalledApplicationList</string>
    <key>InstalledApplicationList</key>
    <array>
        <dict>
            <key>AdHocCodeSigned</key>
            <false/>
            <key>AppStoreVendable</key>
            <false/>
            <key>BetaApp</key>
            <false/>
            <key>BundleSize</key>
            <integer>1036288</integer>
            <key>DeviceBasedVPP</key>
            <false/>
            <key>DynamicSize</key>
            <integer>8192</integer>
            <key>ExternalVersionIdentifier</key>
            <integer>0</integer>
            <key>Identifier</key>
            <string>com.acme.myenterpriseapp</string>
            <key>Installing</key>
            <false/>
            <key>IsValidated</key>
            <true/>
            <key>Name</key>
            <string>MyEnterpriseApp</string>
            <key>ShortVersion</key>
            <string>1.0</string>
            <key>Version</key>
            <string>1.0</string>
        </dict>
    </array>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

**All**:

This command lists all apps. The example response shows a subset of the full response.

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>ManagedAppsOnly</key>
        <false/>
        <key>RequestType</key>
        <string>InstalledApplicationList</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_InstalledApplicationList</string>
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
    <string>0001_InstalledApplicationList</string>
    <key>InstalledApplicationList</key>
    <array>
        <dict>
            <key>BundleSize</key>
            <integer>1</integer>
            <key>Identifier</key>
            <string>com.apple.Safari</string>
            <key>Installing</key>
            <false/>
            <key>Name</key>
            <string>Safari</string>
            <key>ShortVersion</key>
            <string>13.1.2</string>
            <key>Version</key>
            <string>13.1.2</string>
        </dict>
        <dict>
            <key>BundleSize</key>
            <integer>1</integer>
            <key>Identifier</key>
            <string>com.apple.Notes</string>
            <key>Installing</key>
            <false/>
            <key>Name</key>
            <string>Notes</string>
            <key>ShortVersion</key>
            <string>4.7</string>
            <key>Version</key>
            <string>4.7</string>
        </dict>
        <dict>
            <key>BundleSize</key>
            <integer>1</integer>
            <key>Identifier</key>
            <string>com.apple.AddressBook</string>
            <key>Installing</key>
            <false/>
            <key>Name</key>
            <string>Contacts</string>
            <key>ShortVersion</key>
            <string>12.0</string>
            <key>Version</key>
            <string>12.0</string>
        </dict>
        <dict>
            <key>BundleSize</key>
            <integer>1</integer>
            <key>Identifier</key>
            <string>com.apple.mail</string>
            <key>Installing</key>
            <false/>
            <key>Name</key>
            <string>Mail</string>
            <key>ShortVersion</key>
            <string>13.4</string>
            <key>Version</key>
            <string>13.4</string>
        </dict>
        <dict>
            <key>BundleSize</key>
            <integer>1</integer>
            <key>Identifier</key>
            <string>com.apple.iCal</string>
            <key>Installing</key>
            <false/>
            <key>Name</key>
            <string>Calendar</string>
            <key>ShortVersion</key>
            <string>11.0</string>
            <key>Version</key>
            <string>11.0</string>
        </dict>
    </array>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>91FE0F6E-F91C-589A-95E6-02835CE7126D</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object InstalledApplicationListCommand](installedapplicationlistcommand.md)
  The command to get a list of the installed apps on a device.
- [object InstalledApplicationListResponse](installedapplicationlistresponse.md)
  A response from the device after it processes the command to get a list of the installed apps on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Installed Application List Command.

## See Also

- [Install Application](install-application-command.md)
  Install a third-party app on a device.
- [Install Enterprise Application](install-enterprise-application-command.md)
  Install an enterprise app on a device.
- [Managed Application List](managed-application-list-command.md)
  Get the status of all managed apps on a device.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/installed-application-list-command)*