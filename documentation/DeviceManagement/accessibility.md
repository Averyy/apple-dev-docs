# Accessibility

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the accessibility features of the device.

**Availability**:
- macOS 10.9+

## Declaration

```swift
object Accessibility
```

#### Discussion

Specify `com.apple.universalaccess` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
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
            <key>stickyKey</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.myaccessibilitypayload</string>
            <key>PayloadType</key>
            <string>com.apple.universalaccess</string>
            <key>PayloadUUID</key>
            <string>bff2939d-cb4c-4f6d-8521-e26bc7c03e96</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Accessibility</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>e7b55cc7-0d94-4045-8868-dcc1b1c58159</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Properties

- `closeViewFarPoint` (integer): The minimum zoom level in the Zoom options.
- `closeViewHotkeysEnabled` (boolean): If `true`, enables “Use keyboard shortcuts” in the Zoom options.
- `closeViewNearPoint` (integer): The maximum zoom level in the Zoom options.
- `closeViewScrollWheelToggle` (boolean): If `true`, enables “Use scroll gesture” in the Zoom options.
- `closeViewShowPreview` (boolean): If `true`, enables “Show preview rectangle” in the Zoom options. Only available in macOS 10.15 and earlier.
- `closeViewSmoothImages` (boolean): If `true`, enables “Smooth images” in the Zoom options.
- `contrast` (number): The contrast value in the Display options.
- `flashScreen` (boolean): If `true`, enables “Flash the screen” in the Audio options.
- `grayscale` (boolean): If `true`, enables “Use grayscale” in the Display options. This option is deprecated in macOS 11.
- `mouseDriver` (boolean): If `true`, enables Mouse Keys in the Mouse & Trackpad options.
- `mouseDriverCursorSize` (integer): The size of the cursor.
- `mouseDriverIgnoreTrackpad` (boolean): If `true`, ignores the built-in trackpad.
- `mouseDriverInitialDelay` (integer): The initial delay before moving the mouse with Mouse Keys.
- `mouseDriverMaxSpeed` (integer): The maximum speed for the cursor when using Mouse Keys.
- `slowKey` (boolean): If `true`, enables “Slow Keys” in the Keyboard options.
- `slowKeyBeepOn` (boolean): If `true`, enables “click key sounds” for Slow Keys.
- `slowKeyDelay` (integer): The acceptance delay, in milliseconds, for Slow Keys.
- `stereoAsMono` (boolean): If `true`, plays stereo audio as mono.
- `stickyKey` (boolean): If `true`, enables Sticky Keys in the Keyboard options.
- `stickyKeyBeepOnModifier` (boolean): If `true`, enables the beep when a modifier key is set for Sticky Keys.
- `stickyKeyShowWindow` (boolean): If `true`, enables “Display pressed keys on screen” for Sticky Keys.
- `voiceOverOnOffKey` (boolean): If `true`, enables Voice Over.
- `whiteOnBlack` (boolean): If `true`, enables Invert Colors in Display Accommodations.

## See Also

- [object Desktop](desktop.md)
  The payload that configures the desktop wallpaper.
- [object Dock](dock.md)
  The payload that configures the Dock.
- [object Finder](finder.md)
  The payload that configures Finder settings.
- [object HomeScreenLayout](homescreenlayout.md)
  The payload that configures the Home Screen layout.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accessibility)*