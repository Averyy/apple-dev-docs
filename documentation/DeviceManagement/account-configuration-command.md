# Account Configuration

**Framework**: Device Management  
**Kind**: httpRequest

Create and configure a local administrator account on a device.

**Availability**:
- macOS 10.11+

## Mentions

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
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
        <key>AutoSetupAdminAccounts</key>
        <array>
            <dict>
                <key>fullName</key>
                <string>Administrator</string>
                <key>hidden</key>
                <false/>
                <key>shortName</key>
                <string>admin</string>
                <key>passwordHash</key>
                <data>
                    PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4K
                    PCFET0NUWVBFIHBsaXN0IFBVQkxJQyAiLS8vQXBwbGUvL0RURCBQ
                    TElTVCAxLjAvL0VOIiAiaHR0cDovL3d3dy5hcHBsZS5jb20vRFRE
                    cy9Qcm9wZXJ0eUxpc3QtMS4wLmR0ZCI+CjxwbGlzdCB2ZXJzaW9u
                    PSIxLjAiPgo8ZGljdD4KCTxrZXk+U0FMVEVELVNIQTUxMi1QQktE
                    RjI8L2tleT4KCTxkaWN0PgoJCTxrZXk+ZW50cm9weTwva2V5PgoJ
                    CTxkYXRhPgoJCXJiSXZtVGlQQlJ3cWZ6dmFQQnhPT1VLRHVnTnRM
                    YVVQZ2lIVnpBUWNsNDNjSmUzaGZ6ZW05TDVhczAyRQoJCXp2TEFl
                    aTJFT0tqMFNaOENpKzNXV0tQN2orMklSdWU0T1ZyTzBsYnhGOHR5
                    K3pZb0hTMTVRU3hGcUplagoJCU5qdkk1NTk1N1JjZUVLaXFSRjZ1
                    UEpQUTYvbUxEc0xnSTR4dko3NVpEa0JlYW51QkI0TT0KCQk8L2Rh
                    dGE+CgkJPGtleT5zYWx0PC9rZXk+CgkJPGRhdGE+CgkJTXVpS2g1
                    MjR3QkJMV0ZoQ3lzRFIzRnJPOGM0WlFIUGZTRE5JbDZvQjlCST0K
                    CQk8L2RhdGE+CgkJPGtleT5pdGVyYXRpb25zPC9rZXk+CgkJPGlu
                    dGVnZXI+NDAwMDA8L2ludGVnZXI+Cgk8L2RpY3Q+CjwvZGljdD4K
                    PC9wbGlzdD4K
                </data>
            </dict>
        </array>
        <key>DontAutoPopulatePrimaryAccountInfo</key>
        <false/>
        <key>LockPrimaryAccountInfo</key>
        <true/>
        <key>PrimaryAccountFullName</key>
        <string>User</string>
        <key>PrimaryAccountUserName</key>
        <string>user</string>
        <key>RequestType</key>
        <string>AccountConfiguration</string>
        <key>SetPrimarySetupAccountAsRegularUser</key>
        <true/>
        <key>SkipPrimarySetupAccountCreation</key>
        <false/>
    </dict>
    <key>CommandUUID</key>
    <string>0001_AccountConfiguration</string>
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
    <string>0001_AccountConfiguration</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>91FE0F6E-F91C-589A-95E6-02835CE7126D</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object AccountConfigurationCommand](accountconfigurationcommand.md)
  The command to create and configure a local administrator account on a device.
- [object AccountConfigurationResponse](accountconfigurationresponse.md)
  A response from the device after it processes the command to create and configure a local administrator account on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#AccountConfigurationCommand`

## Request Body

The request object the server returns for the Account Configuration Command.

## See Also

- [Invite To Program](invite-to-program-command.md)
  Invite a user to join the Volume Purchase Program (VPP).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/account-configuration-command)*