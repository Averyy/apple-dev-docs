# Remove Media

**Framework**: Device Management  
**Kind**: httpRequest

Remove a previously installed book from a device.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- Device Assignment Services ?+
- VPP License Management ?+

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
    <key>MediaType</key>
    <string>Book</string>
    <key>PersistentID</key>
    <string>com.acme.pdf.myenterprisebook</string>
    <key>RequestType</key>
    <string>RemoveMedia</string>
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
    <string>0001_RemoveMedia</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object RemoveMediaCommand](removemediacommand.md)
  The command to remove a previously installed book from a device.
- [object RemoveMediaResponse](removemediaresponse.md)
  A response from the device after it processes the command to remove a previously installed book from a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#RemoveMediaCommand`

## Request Body

The request object the server returns for the Remove Media Command.

## See Also

- [Install Media](install-media-command.md)
  Install a book on a device.
- [Managed Media List](managed-media-list-command.md)
  Get a list of the managed books on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/remove-media-command)*