# Verify Recovery Lock

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Verify the device’s Recovery Lock password.

**Availability**:
- macOS 11.5+

#### Discussion

This command is only available on a Mac with Apple silicon.

##### Command availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | N/A |
| Requires supervision | macOS |
| Allowed in user enrollment | N/A |
| Required access right | DeviceLockAndRemovePasscode |

##### Example request and response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>RequestType</key>
        <string>VerifyRecoveryLock</string>
        <key>Password</key>
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
    <string>0001_VerifyRecoveryLock</string>
    <key>PasswordVerified</key>
    <true/>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>1AC99473-AE6F-5E59-BE5C-410D257D481E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object VerifyRecoveryLockCommand](./verifyrecoverylockcommand.md)
  The command to verify the device’s Recovery Lock password.
- [object VerifyRecoveryLockResponse](./verifyrecoverylockresponse.md)
  A response from the device after it processes the command to verify the device’s Recovery Lock password.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

**Content-Type**: `application/x-apple-aspen-mdm`  
**Type**: `VerifyRecoveryLockCommand`

The request object the server returns for the Verify Recovery Lock Command.

## Responses

- `200` OK (`VerifyRecoveryLockResponse`, `application/xml`): The response object the system returns for the Verify Recovery Lock Command.

## See Also

### Recovery Lock
- [Set Recovery Lock](./set-recovery-lock-command.md)
  Set or clear the Recovery Lock password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/verify-recovery-lock-command)*