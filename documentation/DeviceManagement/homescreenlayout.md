# HomeScreenLayout

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure the Home screen layout.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- tvOS 11.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object HomeScreenLayout
```

#### Discussion

Specify `com.apple.homescreenlayout` as the payload type.

This payload defines a layout of apps, folders, and web clips for the Home screen. On iOS, this layout is locked and can’t be modified by the user.

If a home screen layout puts more than four items in the iPhone or iPod touch dock the location of the fifth and succeeding items may be undefined but they will not be omitted.

To disable deletion of apps, set `allowAppRemoval` to `false` with [`Restrictions`](restrictions.md).

##### Profile Availability

|  |  |
| --- | --- |
| Device Channel | iOS, Shared iPad, tvOS |
| User Channel | Shared iPad |
| Allow Manual Install | iOS, tvOS |
| Requires Supervision | iOS, tvOS |
| Requires User Approved MDM | - |
| Allowed in User Enrollment | - |
| Allow Multiple Payloads | - |

##### Profile Example

```None
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
  The payload you use to configure the accessibility features of the device.
- [object Desktop](desktop.md)
  The payload you use to configure the desktop.
- [object Dock](dock.md)
  The payload you use to configure the dock.
- [object Finder](finder.md)
  The payload you use to configure Finder settings.
- [object ManagedMenuExtras](managedmenuextras.md)
  The payload you use to configure menu extras.
- [object Notifications](notifications.md)
  The payload you use to configure notifications.
- [object ScreensaverUser](screensaveruser.md)
  The payload you use to configure a user’s screen-saver settings.
- [object SetupAssistant](setupassistant.md)
  The payload you use to configure setup-assistant settings.
- [object TimeMachine](timemachine.md)
  The payload you use to configure Time Machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/homescreenlayout)*