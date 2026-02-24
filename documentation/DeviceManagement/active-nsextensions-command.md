# Active NSExtensions

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of active extensions for a user on a device.

**Availability**:
- macOS 10.13+

#### Discussion

This command returns information about the active extensions for a user. Extensions exist for each user, not for the device.

Extensions restricted from executing by Application Launch Restrictions or the [`NSExtensionManagement`](nsextensionmanagement.md) configuration profile won’t appear in the response.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | NA |
| User channel | macOS |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | QueryInstalledApps |

##### Example Request and Response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>FilterExtensionPoints</key>
        <array>
            <string>com.apple.share-services</string>
        </array>
        <key>RequestType</key>
        <string>ActiveNSExtensions</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ActiveNSExtensions</string>
</dict>
</plist>
```

**Response**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>ActiveNSExtensions</key>
    <array>
        <dict>
            <key>ContainerDisplayName</key>
            <string>Messages.app</string>
            <key>ContainerIdentifier</key>
            <string>com.apple.iChat</string>
            <key>DisplayName</key>
            <string>Messages</string>
            <key>ExtensionPoint</key>
            <string>com.apple.share-services</string>
            <key>Identifier</key>
            <string>com.apple.messages.ShareExtension</string>
            <key>Path</key>
            <string>/System/Applications/Messages.app/Contents/PlugIns/Messages Share Extension.appex</string>
            <key>UserElection</key>
            <string>Use</string>
            <key>Version</key>
            <string>1.0</string>
        </dict>
        <dict>
            <key>DisplayName</key>
            <string>Set Background Image</string>
            <key>ExtensionPoint</key>
            <string>com.apple.share-services</string>
            <key>Identifier</key>
            <string>com.apple.share.System.set-desktop-image</string>
            <key>Path</key>
            <string>/System/Library/PrivateFrameworks/ShareKit.framework/Versions/A/PlugIns/SystemSetDesktopImage.appex</string>
            <key>UserElection</key>
            <string>Use</string>
            <key>Version</key>
            <string>639</string>
        </dict>
        <dict>
            <key>DisplayName</key>
            <string>Add to Reading List</string>
            <key>ExtensionPoint</key>
            <string>com.apple.share-services</string>
            <key>Identifier</key>
            <string>com.apple.share.System.add-to-safari-reading-list</string>
            <key>Path</key>
            <string>/System/Library/PrivateFrameworks/ShareKit.framework/Versions/A/PlugIns/SystemAddToReadingList.appex</string>
            <key>UserElection</key>
            <string>Use</string>
            <key>Version</key>
            <string>639</string>
        </dict>
    </array>
    <key>CommandUUID</key>
    <string>0001_ActiveNSExtensions</string>
    <key>NotOnConsole</key>
    <false/>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>E84CD517-CB37-52F7-988C-DB5137B604B8</string>
    <key>UserID</key>
    <string>03EBB586-53E7-48CE-8E6E-C54A374F6FA6</string>
    <key>UserLongName</key>
    <string>admin</string>
    <key>UserShortName</key>
    <string>admin</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object ActiveNSExtensionsCommand](activensextensionscommand.md)
  The command to get a list of active extensions for a user on a device.
- [object ActiveNSExtensionsResponse](activensextensionsresponse.md)
  A response from the device after it processes the command to get a list of active extensions for a user on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Active NSExtensions Command.

## See Also

- [NSExtension Mappings](nsextension-mappings-command.md)
  Get a list of the installed extensions for a user on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/active-nsextensions-command)*