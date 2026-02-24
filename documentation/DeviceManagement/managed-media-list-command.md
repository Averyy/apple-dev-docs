# Managed Media List

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of the managed books on a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | iOS |
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
        <string>ManagedMediaList</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ManagedMediaList</string>
</dict>
</plist>
```

**Response**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Books</key>
    <array>
        <dict>
            <key>Author</key>
            <string>Acme, Inc.</string>
            <key>Kind</key>
            <string>pdf</string>
            <key>PersistentID</key>
            <string>com.acme.pdf.myenterprisebook</string>
            <key>State</key>
            <string>Managed</string>
            <key>Title</key>
            <string>My Enterprise Book</string>
            <key>Version</key>
            <string>1.0</string>
        </dict>
    </array>
    <key>CommandUUID</key>
    <string>0001_ManagedMediaList</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object ManagedMediaListCommand](managedmedialistcommand.md)
  The command to get a list of the managed books on a device.
- [object ManagedMediaListResponse](managedmedialistresponse.md)
  A response from the device after it processes the command to get a list of the managed books on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Managed Media List Command.

## See Also

- [Install Media](install-media-command.md)
  Install a book on a device.
- [Remove Media](remove-media-command.md)
  Remove a previously installed book from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managed-media-list-command)*