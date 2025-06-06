# ServiceManagementManagedLoginItems

**Framework**: Device Management  
**Kind**: dictionary

This payload you use to configure managed login items, which auto-enables and auto-allows matched items.

**Availability**:
- macOS 13.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ServiceManagementManagedLoginItems
```

#### Discussion

Specify `com.apple.servicemanagement` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | macOS |
| User Channel | - |
| Allow Manual Install | - |
| Requires Supervision | - |
| Requires User Approved MDM | macOS |
| Allowed in User Enrollment | - |
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
            <key>PayloadIdentifier</key>
            <string>com.example.myservicemanagementpayload</string>
            <key>PayloadUUID</key>
            <string>0d4e2ece-dfa7-4103-97ff-e91a9f842a1d</string>
            <key>PayloadType</key>
            <string>com.apple.servicemanagement</string>
            <key>Rules</key>
            <array>
                <dict>
                    <key>RuleType</key>
                    <string>BundleIdentifier</string>
                    <key>RuleValue</key>
                    <string>com.example.myapp</string>
                    <key>Comment</key>
                    <string>My Example App</string>
                </dict>
                <dict>
                    <key>RuleType</key>
                    <string>BundleIdentifierPrefix</string>
                    <key>RuleValue</key>
                    <string>com.example</string>
                    <key>Comment</key>
                    <string>All apps from Example</string>
                </dict>
                <dict>
                    <key>RuleType</key>
                    <string>Label</string>
                    <key>RuleValue</key>
                    <string>com.example.internal.tool</string>
                    <key>Comment</key>
                    <string>Job to run an internal task here at Example</string>
                </dict>
                <dict>
                    <key>RuleType</key>
                    <string>LabelPrefix</string>
                    <key>RuleValue</key>
                    <string>com.example</string>
                    <key>Comment</key>
                    <string>All jobs to run internal tasks here at Example</string>
                </dict>
                <dict>
                    <key>RuleType</key>
                    <string>TeamIdentifier</string>
                    <key>RuleValue</key>
                    <string>ABCDE12345</string>
                    <key>Comment</key>
                    <string>Another way to specify all apps from Example</string>
                </dict>
            </array>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Service Management</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadUUID</key>
    <string>03cca12c-a610-44c2-96f9-fdabe3acd47d</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadScope</key>
    <string>System</string>
</dict>
</plist>

```

## Topics

### Supporting Objects
- [object ServiceManagementManagedLoginItems.Rule](servicemanagementmanagedloginitems/rule.md)
  A dictionary that configures a service management rule.

## See Also

- [object LoginItemsManagedItems](loginitemsmanageditems.md)
  The payload you use to configure a device’s login items.
- [object LoginWindowLoginItems](loginwindowloginitems.md)
  The payload you use to configure login behavior.
- [object LoginWindow](loginwindow.md)
  The payload you use to configure login window behavior.
- [object LoginWindowScripts](loginwindowscripts.md)
  The payload you use to configure scripts to run at login and logout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/servicemanagementmanagedloginitems)*