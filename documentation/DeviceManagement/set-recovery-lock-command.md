# Set Recovery Lock

**Framework**: Device Management  
**Kind**: httpRequest

Set or clear the Recovery Lock password.

**Availability**:
- macOS 11.5+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command sets, or clears, a password on booting to recoveryOS. When the device unenrolls MDM the system removes the recovery password.

This command is only available on a Mac with Apple silicon.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | DeviceLockAndRemovePasscode |

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
        <string>SetRecoveryLock</string>
        <key>NewPassword</key>
        <string>Apple</string>
    </dict>
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
    <string>0001_SetRecoveryLock</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>1AC99473-AE6F-5E59-BE5C-410D257D481E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object SetRecoveryLockCommand](setrecoverylockcommand.md)
  The command to set or clear the Recovery Lock password.
- [object SetRecoveryLockResponse](setrecoverylockresponse.md)
  A response from the device after it processes the command to set or clear the Recovery Lock password.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#SetRecoveryLockCommand`

## Request Body

The request object the server returns for the Set Recovery Lock Command.

## See Also

- [Verify Recovery Lock](verify-recovery-lock-command.md)
  Verify the device’s Recovery Lock password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/set-recovery-lock-command)*