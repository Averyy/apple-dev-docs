# User List

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of users with active accounts on a device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- macOS 10.13+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | NA |

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
        <string>UserList</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_UserList</string>
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
    <string>0001_UserList</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>cf98820bd143abe0bbf151bed8e8e427594d2f88</string>
    <key>Users</key>
    <array>
        <dict>
            <key>DataQuota</key>
            <integer>10171187200</integer>
            <key>DataUsed</key>
            <integer>145625088</integer>
            <key>HasDataToSync</key>
            <true/>
            <key>IsLoggedIn</key>
            <false/>
            <key>UserName</key>
            <string>example@acme.com</string>
        </dict>
    </array>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object UserListCommand](userlistcommand.md)
  The command to get a list of users with active accounts on a device.
- [object UserListResponse](userlistresponse.md)
  A response from the device after it processes the command to get a list of users with active accounts on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the User List Command.

## See Also

- [Log Out User](log-out-user-command.md)
  Force the current user to log out of a device.
- [Delete User](delete-user-command.md)
  Delete a user’s account from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/user-list-command)*