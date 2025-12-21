# LoginItemsManagedItems

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures a device’s login items.

**Availability**:
- macOS 10.13+

## Declaration

```swift
object LoginItemsManagedItems
```

#### Discussion

Specify `com.apple.loginitems.managed` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | macOS |
| Allow multiple payloads | macOS |

##### Profile Example

```plist
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
  The payload that configures login behavior.
- [object LoginWindow](loginwindow.md)
  The payload that configures Login Window behavior.
- [object LoginWindowScripts](loginwindowscripts.md)
  The payload that configures scripts to run at login and logout.
- [object ServiceManagementManagedLoginItems](servicemanagementmanagedloginitems.md)
  This payload that configures managed login items, which auto-enables and auto-allows matched items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/loginitemsmanageditems)*