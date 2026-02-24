# Declarative Management

**Framework**: Device Management  
**Kind**: httpRequest

Enable your server to support declarative management or trigger a declarative management synchronization operation on the device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

The server uses this command to turn on the declarative management engine on the device the first time the server sends it. Subsequent commands trigger a declarative management synchronization operation.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right |  |

##### Example Request and Response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>CommandUUID</key>
        <string>0001_DeclarativeManagement</string>
        <key>Command</key>
        <dict>
            <key>RequestType</key>
            <string>DeclarativeManagement</string>
            <key>Data</key>
            <data>
            eyJTeW5jVG9rZW5zIjogeyJUaW1lc3RhbXAiOiAiMjAyMS0wNi0wMlQwMToy
            ODowMFoiLCAiRGVjbGFyYXRpb25zVG9rZW4iOiAiYjY1NDQwMjdhMzE1Y2Qw
            MDg1ZDRjZjA4MTc0NjI0YzJkMTQyNDQ0ODA0MzBhODdiMTc2YTI3MjdlNzM2
            NjEzOCJ9fQ==
            </data>
        </dict>
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
    <string>0001_DeclarativeManagement</string>
    <key>EnrollmentID</key>
    <string>8DB29EAB-A5BB-4B60-8DDA-F75517766FAC</string>
    <key>Status</key>
    <string>Acknowledged</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object DeclarativeManagementCommand](declarativemanagementcommand.md)
  The command to enable your server to support declarative management or trigger a declarative management synchronization operation on the device.
- [object DeclarativeManagementResponse](declarativemanagementresponse.md)
  A response from the device after it processes the command to enable your server to support declarative management or trigger a declarative management synchronization operation on the device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Declarative Management Command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarative-management-command)*