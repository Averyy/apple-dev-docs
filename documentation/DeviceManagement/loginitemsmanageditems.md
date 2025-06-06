# LoginItemsManagedItems

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure a device’s login items.

**Availability**:
- macOS 10.13+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object LoginItemsManagedItems
```

#### Discussion

Specify `com.apple.loginitems.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | macOS |
| Allow Manual Install | macOS |
| Requires Supervision | - |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | macOS |
| Allow Multiple Payloads | macOS |

##### Profile Example

```None
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AutoLaunchedApplicationDictionary-managed</key>
            <array>
                <dict>
                    <key>Path</key>
                    <string>/System/Applications/Example.app</string>
                    <key>Hide</key>
                    <false/>
                </dict>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.myloginitemsmanageditemspayload</string>
            <key>PayloadType</key>
            <string>com.apple.loginitems.managed</string>
            <key>PayloadUUID</key>
            <string>f19d4636-fa34-4a7c-8e8b-e92de516c893</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Login Items Managed Items</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>98128de8-d76c-44fa-9509-5601c0d66281</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object LoginItemsManagedItems.LoginItem](loginitemsmanageditems/loginitem.md)
  A dictionary with the details about a login item.

## See Also

- [object LoginWindowLoginItems](loginwindowloginitems.md)
  The payload you use to configure login behavior.
- [object LoginWindow](loginwindow.md)
  The payload you use to configure login window behavior.
- [object LoginWindowScripts](loginwindowscripts.md)
  The payload you use to configure scripts to run at login and logout.
- [object ServiceManagementManagedLoginItems](servicemanagementmanagedloginitems.md)
  This payload you use to configure managed login items, which auto-enables and auto-allows matched items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/loginitemsmanageditems)*