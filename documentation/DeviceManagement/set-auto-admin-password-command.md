# Set Auto Admin Password

**Framework**: Device Management  
**Kind**: httpRequest

Update the local administrator account password.

**Availability**:
- macOS 10.11+
- Device Assignment Services ?+
- VPP License Management ?+

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
        <key>GUID</key>
        <string>F7C60A02-E0AB-4C87-8356-E0CC11568043</string>
        <key>RequestType</key>
        <string>SetAutoAdminPassword</string>
        <key>passwordHash</key>
        <data>
            PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4K
            PCFET0NUWVBFIHBsaXN0IFBVQkxJQyAiLS8vQXBwbGUvL0RURCBQ
            TElTVCAxLjAvL0VOIiAiaHR0cDovL3d3dy5hcHBsZS5jb20vRFRE
            cy9Qcm9wZXJ0eUxpc3QtMS4wLmR0ZCI+CjxwbGlzdCB2ZXJzaW9u
            PSIxLjAiPgo8ZGljdD4KCTxrZXk+U0FMVEVELVNIQTUxMi1QQktE
            RjI8L2tleT4KCTxkaWN0PgoJCTxrZXk+ZW50cm9weTwva2V5PgoJ
            CTxkYXRhPgoJCVpxcWVkTU5Ya3BtVjhEbU5iRFdUYjBHTDNSNjAz
            RHNVSllkb1BvV0NlK2gwRDNubC9mWCsxTlpKSUxPdgoJCTBxQTVC
            Q0FBSEZCZ3REQzVqeEF3a2NyZ1puZVd4eWpGZGpvT0hsV2RoYWVF
            T0MyaFBwVktIaC9WUk9uUQoJCXM2cWUvRGtaZ1djVDBQdk9VQ3NM
            ZVhTd2dOTU9UNGFwMnJWR0IxOVFwSFBpdnJrNmp2dz0KCQk8L2Rh
            dGE+CgkJPGtleT5pdGVyYXRpb25zPC9rZXk+CgkJPGludGVnZXI+
            NDAwMDA8L2ludGVnZXI+CgkJPGtleT5zYWx0PC9rZXk+CgkJPGRh
            dGE+CgkJZUl3Q3hxUk1NVm0wWGZ3VmpvbERCNEFUc2I0K3ZWMjdL
            Z1hDdU5ZMkNlOD0KCQk8L2RhdGE+Cgk8L2RpY3Q+CjwvZGljdD4K
            PC9wbGlzdD4K
        </data>
    </dict>
    <key>CommandUUID</key>
    <string>0001_SetAutoAdminPassword</string>
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
    <string>0001_SetAutoAdminPassword</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>91FE0F6E-F91C-589A-95E6-02835CE7126D</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object SetAutoAdminPasswordCommand](setautoadminpasswordcommand.md)
  The command to update the local administrator account password.
- [object SetAutoAdminPasswordResponse](setautoadminpasswordresponse.md)
  A response from the device after it processes the command to update the local administrator account password.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#SetAutoAdminPasswordCommand`

## Request Body

The request object the server returns for the Set Auto Admin Password Command.

## See Also

- [Clear Passcode](clear-passcode-command.md)
  Remove the passcode from a device.
- [Clear Restrictions Password](clear-restrictions-password-command.md)
  Clear the Screen Time password and the restrictions on a device.
- [Unlock User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/set-auto-admin-password-command)*