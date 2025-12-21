# HomeScreenLayout

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the Home Screen layout.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- tvOS 11.0+

## Declaration

```swift
object HomeScreenLayout
```

#### Discussion

Specify `com.apple.homescreenlayout` as the payload type.

This payload defines a layout of apps, folders, and web clips for the Home Screen. This layout is locked and can’t be modified by the user.

If a Home Screen layout puts more than four items in the iPhone Dock the location of the fifth and succeeding items may be undefined but they will not be omitted.

To disable deletion of apps, set `allowAppRemoval` to `false` with [`Restrictions`](restrictions.md).

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad, tvOS |
| User channel | Shared iPad |
| Allow manual install | iOS, tvOS |
| Requires supervision | iOS, tvOS |
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
            <key>Dock</key>
            <array>
                <dict>
                    <key>Type</key>
                    <string>Application</string>
                    <key>BundleID</key>
                    <string>com.apple.mobilesafari</string>
                </dict>
                <dict>
                    <key>Type</key>
                    <string>Application</string>
                    <key>BundleID</key>
                    <string>com.apple.Preferences</string>
                </dict>
                <dict>
                    <key>Type</key>
                    <string>Folder</string>
                    <key>DisplayName</key>
                    <string>Example</string>
                    <key>Pages</key>
                    <array>
                        <array>
                            <dict>
                                <key>Type</key>
                                <string>WebClip</string>
                                <key>DisplayName</key>
                                <string>Example</string>
                                <key>URL</key>
                                <string>companyname.com</string>
                            </dict>
                        </array>
                        <array>
                            <dict>
                                <key>Type</key>
                                <string>Application</string>
                                <key>BundleID</key>
                                <string>com.apple.News</string>
                            </dict>
                        </array>
                    </array>
                </dict>
            </array>
            <key>Pages</key>
            <array>
                <array>
                    <dict>
                        <key>Type</key>
                        <string>Application</string>
                        <key>BundleID</key>
                        <string>com.apple.MobileSMS</string>
                    </dict>
                    <dict>
                        <key>Type</key>
                        <string>Application</string>
                        <key>BundleID</key>
                        <string>com.apple.camera</string>
                    </dict>
                    <dict>
                        <key>Type</key>
                        <string>Folder</string>
                        <key>DisplayName</key>
                        <string>Display Name exampler</string>
                        <key>Pages</key>
                        <array>
                            <array>
                                <dict>
                                    <key>Type</key>
                                    <string>Application</string>
                                    <key>BundleID</key>
                                    <string>com.apple.podcasts</string>
                                </dict>
                            </array>
                        </array>
                    </dict>
                    <dict>
                        <key>Type</key>
                        <string>WebClip</string>
                        <key>URL</key>
                        <string>https://www.apple.com</string>
                        <key>DisplayName</key>
                        <string>Custom Home Screen Layout</string>
                    </dict>
                    <dict>
                        <key>Type</key>
                        <string>Application</string>
                        <key>BundleID</key>
                        <string>com.apple.AppStore</string>
                    </dict>
                </array>
                <array>
                    <dict>
                        <key>Type</key>
                        <string>Folder</string>
                        <key>DisplayName</key>
                        <string>Important Folder</string>
                    </dict>
                    <dict>
                        <key>Type</key>
                        <string>Application</string>
                        <key>BundleID</key>
                        <string>com.apple.Bridge</string>
                    </dict>
                </array>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.myhomescreenlayoutpayload</string>
            <key>PayloadType</key>
            <string>com.apple.homescreenlayout</string>
            <key>PayloadUUID</key>
            <string>f0b2d13e-a985-4264-9901-707feabddfcd</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Home Screen Layout</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>24c41ae0-f8a9-4d9f-a007-d67b0dc15af4</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object HomeScreenLayout.IconItem](homescreenlayout/iconitem.md)
  An array of dictionaries that conform to the icon dictionary format.

## See Also

- [object Accessibility](accessibility.md)
  The payload that configures the accessibility features of the device.
- [object Desktop](desktop.md)
  The payload that configures the desktop wallpaper.
- [object Dock](dock.md)
  The payload that configures the Dock.
- [object Finder](finder.md)
  The payload that configures Finder settings.
- [object ManagedMenuExtras](managedmenuextras.md)
  The payload that configures menu extras.
- [object Notifications](notifications.md)
  The payload that configures notifications.
- [object ScreensaverUser](screensaveruser.md)
  The payload that configures a user’s screen saver settings.
- [object SetupAssistant](setupassistant.md)
  The payload that configures Setup Assistant settings.
- [object TimeMachine](timemachine.md)
  The payload that configures Time Machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/homescreenlayout)*