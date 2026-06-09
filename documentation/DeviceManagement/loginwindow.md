# LoginWindow

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures Login Window behavior.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object LoginWindow
```

#### Discussion

Specify `com.apple.loginwindow` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | N/A |
| Allow manual install | macOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
| Allowed in user enrollment | N/A |
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
            <key>AdminHostInfo</key>
            <string>HostName</string>
            <key>AdminMayDisableMCX</key>
            <true/>
            <key>AllowList</key>
            <array/>
            <key>AlwaysShowWorkgroupDialog</key>
            <true/>
            <key>CombineUserWorkgroups</key>
            <true/>
            <key>DenyList</key>
            <array/>
            <key>DisableConsoleAccess</key>
            <true/>
            <key>EnableExternalAccounts</key>
            <false/>
            <key>FlattenUserWorkgroups</key>
            <true/>
            <key>HideAdminUsers</key>
            <false/>
            <key>HideLocalUsers</key>
            <false/>
            <key>HideMobileAccounts</key>
            <false/>
            <key>IncludeNetworkUser</key>
            <true/>
            <key>LocalUserLoginEnabled</key>
            <true/>
            <key>LocalUsersHaveWorkgroups</key>
            <true/>
            <key>RestartDisabled</key>
            <false/>
            <key>RetriesUntilHint</key>
            <integer>0</integer>
            <key>SHOWFULLNAME</key>
            <false/>
            <key>SHOWOTHERUSERS_MANAGED</key>
            <true/>
            <key>ShutDownDisabled</key>
            <false/>
            <key>SleepDisabled</key>
            <false/>
            <key>UseComputerNameForComputerRecordName</key>
            <true/>
            <key>com.apple.login.mcx.DisableAutoLoginClient</key>
            <true/>
            <key>showInputMenu</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.myloginwindowpayload</string>
            <key>PayloadType</key>
            <string>com.apple.loginwindow</string>
            <key>PayloadUUID</key>
            <string>fe9ba3c5-0f1a-45c7-b6df-a5f4489695fe</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Login Window</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>61bd7d63-4a4a-4b67-9112-5ceb16afb4dc</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `AdminHostInfo` (string): The admin host info. If present in the payload, the system displays its value in the Login Window as additional computer information. Before macOS 10.10, this string could only contain host name, system version, or IP address. After macOS 10.10, setting this key to any value allows the user to click the time area of the menu bar to toggle through various computer information values.
- `AllowList` ([string]): The list of user GUIDs or group GUIDs of users that the system allows to log in. An asterisk (`*`) string specifies all users or groups. This only applies to network accounts and mobile accounts.
- `AutologinPassword` (string): An optional user password to set up auto login. This must match the `AutologinUsername` user’s current password. Available: macOS 14+
- `AutologinUsername` (string): The user short name for an existing user to set up auto login. Available: macOS 14+
- `DenyList` ([string]): The list of user GUIDs or group GUIDs of users that the system disallows to log in. This list takes priority over the list in the `AllowList` key. This only applies to network accounts and mobile accounts.
- `DisableConsoleAccess` (boolean): If `true`, the system disregards the `>console` special user name, which provides a command line UI.
- `DisableFDEAutoLogin` (boolean): If `true`, the system disables the automatic login option when using FileVault. Available: macOS 10.9+
- `DisableScreenLockImmediate` (boolean): If `true`, the system disables the immediate Screen Lock functions. Available: macOS 10.13+
- `HideAdminUsers` (boolean): If `true`, the system hides administrator users when showing a user list.
- `HideLocalUsers` (boolean): If `true`, the system shows only network and system users when showing a user list.
- `HideMobileAccounts` (boolean): If `true`, the system hides mobile account users in a user list. In some cases, mobile users show up as network users.
- `IncludeNetworkUser` (boolean): If `true`, the system shows network users when showing a user list.
- `LoginwindowText` (string): The text to display in the Login Window.
- `LogOutDisabledWhileLoggedIn` (boolean): If `true`, the system disables the Log Out menu item when the user is logged in. Available: macOS 10.13+
- `PowerOffDisabledWhileLoggedIn` (boolean): If `true`, the system disables the Power Off menu item when the user is logged in.
- `RestartDisabled` (boolean): If `true`, the system disables the Restart item.
- `RestartDisabledWhileLoggedIn` (boolean): If `true`, the system disables the Restart menu item when the user is logged in.
- `SHOWFULLNAME` (boolean): If `true`, the system shows the name and password dialog. If `false`, the system displays a list of users.
- `showInputMenu` (boolean): If `true`, the system shows the Input Menu in the Login Window. Available: macOS 10.8+
- `SHOWOTHERUSERS_MANAGED` (boolean): If `true`, the system displays “Other…” when it shows a list of users.
- `ShutDownDisabled` (boolean): If `true`, the system disables the Shut Down button.
- `ShutDownDisabledWhileLoggedIn` (boolean): If `true`, the system disables the Shut Down menu item when the user is logged in.
- `SleepDisabled` (boolean): If `true`, the system disables the Sleep button.

## See Also

- [object LoginItemsManagedItems](loginitemsmanageditems.md)
  The payload that configures a device’s login items.
- [object LoginWindowLoginItems](loginwindowloginitems.md)
  The payload that configures login behavior.
- [object LoginWindowScripts](loginwindowscripts.md)
  The payload that configures scripts to run at login and logout.
- [object ServiceManagementManagedLoginItems](servicemanagementmanagedloginitems.md)
  This payload that configures managed login items, which auto-enables and auto-allows matched items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/loginwindow)*