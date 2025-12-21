# LoginWindowLoginItems

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures login behavior.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object LoginWindowLoginItems
```

#### Discussion

Specify `loginwindow` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | NA |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>DisableLoginItemsSuppression</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.myloginwindowloginitemspayload</string>
            <key>PayloadType</key>
            <string>loginwindow</string>
            <key>PayloadUUID</key>
            <string>e032844e-db81-4387-98d9-9ee7c6038275</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Login Window Login Items</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>30724e47-e58e-447d-b21c-a65bbe184f98</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object LoginItemsManagedItems](loginitemsmanageditems.md)
  The payload that configures a device’s login items.
- [object LoginWindow](loginwindow.md)
  The payload that configures Login Window behavior.
- [object LoginWindowScripts](loginwindowscripts.md)
  The payload that configures scripts to run at login and logout.
- [object ServiceManagementManagedLoginItems](servicemanagementmanagedloginitems.md)
  This payload that configures managed login items, which auto-enables and auto-allows matched items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/loginwindowloginitems)*