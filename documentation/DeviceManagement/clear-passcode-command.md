# Clear Passcode

**Framework**: Device Management  
**Kind**: httpRequest

Remove the passcode from a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

Clearing the passcode in iOS 16 no longer adds the passcode to the history of passcodes. Therefore, the user can reuse the cleared passcode even when the `Passcode` payload has the `pinHistory` key set.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, visionOS, watchOS |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | NA |
| Required access right | AllowPasscodeRemovalAndLock |

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
        <string>ClearPasscode</string>
        <key>UnlockToken</key>
        <data>
        REFUQQAABPRWRVJTAAAABAAAAAVUWVBFAAAABAAAAAJVVUlEAAAAEGHX7XgO5UNZsRiL
        9Kq3hSdITUNLAAAAKLUR5mc5hBzI4bEsbWacE/gmhdJS6rl3978V3DY9ylBbEBGgJ/fA
        Ac9XUkFQAAAABAAAAAFTQUxUAAAAFIHju7P8BPFTz0JA8MDo+PsvcAAmSVRFUgAAAAQA
        AEEaVVVJRAAAABC70Oy5TtZCGocX/i7orO/pQ0xBUwAAAAQAAAABV1JBUAAAAAQAAAAD
        S1RZUAAAAAQAAAAAV1BLWQAAACjH8wUEvSkfgrEPSSQUazAz1eCuTXET3CkqgkNQZkjS
        jZEHtWmXpC4IVVVJRAAAABBW4TUxIb1L7aNAmbmGkxiIQ0xBUwAAAAQAAAACV1JBUAAA
        AAQAAAADS1RZUAAAAAQAAAABV1BLWQAAAChaDERvmDXtk9mikMCT30uDQ4XwrT9ifdmf
        3Hjz/6atBPq/1uNpm5TtUEJLWQAAACCypmyEJV4x4wV6CKfZFEmkYHf8kOXh5ONM1A6B
        R26KM1VVSUQAAAAQH5Ol3/mLSM2dLvFxGTlf5kNMQVMAAAAEAAAAA1dSQVAAAAAEAAAA
        A0tUWVAAAAAEAAAAAFdQS1kAAAAoxNNjRWfqvgqXMVyiqDH2LXJdpafgsm+8ovRQuzL4
        tp3Bs5y25bmRelVVSUQAAAAQB7drprzaR5aePknqFUjyWENMQVMAAAAEAAAABVdSQVAA
        AAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAoMCe2S7psda5AHw99a+DKV8m0hR6aKUKP
        VG5oURKAJZSXJKYRRO2xKlVVSUQAAAAQMpEnWAWOS0qnOwWRdtSAlUNMQVMAAAAEAAAA
        BldSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAoyhn4O/EIo5Q1NLt0/wL1UZGA
        EqTE45DEcNstAQZLk+1U/FSKOWtqrlVVSUQAAAAQFuJUehe6TC+3TImCkemk6kNMQVMA
        AAAEAAAAB1dSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAoMcyPJI8vNBh7j6je
        VPu3zgDYTXAuoo68jqZU4kCubSGyRvIpa/O4n1VVSUQAAAAQF2v1dlxfRMqYs7swzn9s
        nENMQVMAAAAEAAAACFdSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAoSx2pMsvH
        K2HNg9IIbrVEzX7T3Rw0vLEmwMJ3ignooj+3GMHeaJ0aplVVSUQAAAAQ8Qif3NCoTjiK
        WRjgOIHG6ENMQVMAAAAEAAAACVdSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQS1kAAAAo
        n2icCfaIRPbE7mzGqO7rOnuPhgUbYkcpAqf6RnAXljcpSxZqBiJtGlVVSUQAAAAQt9a3
        ThB7SwaGw50i9Hhfu0NMQVMAAAAEAAAACldSQVAAAAAEAAAAA0tUWVAAAAAEAAAAAFdQ
        S1kAAAAoEW1/yC+YYXLVzyRxZwghOADACnWvOnHdBPhJ/z7VEkyHcObDPI9w41VVSUQA
        AAAQ4vImTUp5S7qmyMDZ82nM70NMQVMAAAAEAAAAC1dSQVAAAAAEAAAAA0tUWVAAAAAE
        AAAAAFdQS1kAAAAo8vkvhYNP7rTLdfXRifh+dcTIbj3EEJKyYXeCL9J9trYAo7B5mV5u
        41NJR04AAAAUtFVbS3MM33WvBsEis1imzvs069A=
        </data>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ClearPasscode</string>
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
    <string>0001_ClearPasscode</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object ClearPasscodeCommand](clearpasscodecommand.md)
  The command to remove the passcode from a device.
- [object ClearPasscodeResponse](clearpasscoderesponse.md)
  A response from the device after it processes the command to remove the passcode from a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#ClearPasscodeCommand`

## Request Body

The request object the server returns for the Clear Passcode Command.

## See Also

- [Clear Restrictions Password](clear-restrictions-password-command.md)
  Clear the Screen Time password and the restrictions on a device.
- [Unlock User Account](unlock-user-account-command.md)
  Unlock a user account that the system locked because of too many failed password attempts.
- [Set Auto Admin Password](set-auto-admin-password-command.md)
  Update the local administrator account password.
- [Set Firmware Password](set-firmware-password-command.md)
  Change or clear the firmware password on a device.
- [Verify Firmware Password](verify-firmware-password-command.md)
  Verify the firmware password on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clear-passcode-command)*