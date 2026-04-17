# Invite To Program

**Framework**: Device Management  
**Kind**: httpRequest

Invite a user to join the Volume Purchase Program (VPP).

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.9+

#### Discussion

This command allows a server to invite a user to join the Volume Purchase Program (VPP). It issues the invitation, but doesn’t allow the server to monitor whether the user joins the program. This command yields a `NotNow` status if Setup Assistant is running.

The command doesn’t work with Account Driven enrollments.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS |
| User channel | macOS, Shared iPad |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
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
        <key>InvitationURL</key>
        <string>https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/associateVPPUserWithITSAccount?cc=us&amp;inviteCode=7770596534cf46b58fb0254e7112a5e5&amp;mt=8</string>
        <key>ProgramID</key>
        <string>com.apple.cloudvpp</string>
        <key>RequestType</key>
        <string>InviteToProgram</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_InviteToProgram</string>
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
    <string>0001_InviteToProgram</string>
    <key>InvitationResult</key>
    <string>Acknowledged</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object InviteToProgramCommand](invitetoprogramcommand.md)
  The command to invite a user to join the Volume Purchase Program (VPP).
- [object InviteToProgramResponse](invitetoprogramresponse.md)
  A response from the device after it processes the command to invite a user to join the Volume Purchase Program (VPP).

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#InviteToProgramCommand`

## Request Body

The request object the server returns for the Invite To Program Command.

## See Also

- [Account Configuration](account-configuration-command.md)
  Create and configure a local administrator account on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/invite-to-program-command)*