# NSExtension Mappings

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of the installed extensions for a user on a device.

**Availability**:
- macOS 10.13+

#### Discussion

This list is a superset of the list that [`ActiveNSExtensionsCommand`](activensextensionscommand.md) returns. It may contain extensions that the system never enables due to various restrictions.

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
        <key>RequestType</key>
        <string>NSExtensionMappings</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_NSExtensionMappings</string>
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
    <string>0001_NSExtensionMappings</string>
    <key>NSExtensionMappings</key>
    <array>
        <dict>
            <key>DisplayName</key>
            <string>Photos</string>
            <key>ExtensionPoint</key>
            <string>com.apple.storagemanagement</string>
            <key>Identifier</key>
            <string>com.apple.Photos.StorageManagementExtension</string>
        </dict>
        <dict>
            <key>DisplayName</key>
            <string>Messages</string>
            <key>ExtensionPoint</key>
            <string>com.apple.share-services</string>
            <key>Identifier</key>
            <string>com.apple.messages.ShareExtension</string>
        </dict>
        <dict>
            <key>DisplayName</key>
            <string>iCloud Drive</string>
            <key>ExtensionPoint</key>
            <string>com.apple.fileprovider-nonui</string>
            <key>Identifier</key>
            <string>com.apple.CloudDocs.MobileDocumentsFileProvider</string>
        </dict>
        <dict>
            <key>DisplayName</key>
            <string>Notes Spotlight Index Extension</string>
            <key>ExtensionPoint</key>
            <string>com.apple.spotlight.index</string>
            <key>Identifier</key>
            <string>com.apple.Notes.SpotlightIndexExtension</string>
        </dict>
    </array>
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
- [object NSExtensionMappingsCommand](nsextensionmappingscommand.md)
  The command to get a list of the installed extensions for a user on a device.
- [object NSExtensionMappingsResponse](nsextensionmappingsresponse.md)
  A response from the device after it processes the command to get a list of the installed extensions for a user on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#NSExtensionMappingsCommand`

## Request Body

The request object the server returns for the NSExtension Mappings Command.

## See Also

- [Active NSExtensions](active-nsextensions-command.md)
  Get a list of active extensions for a user on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/nsextension-mappings-command)*