# icon

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The custom icon displayed in the alert.

**Availability**:
- macOS

## Declaration

```swift
var icon: NSImage! { get set }
```

```objc
@property (strong, null_resettable) NSImage * icon;
```

## Discussion

By default, the image used in an alert is the app icon. If you set this property’s value, your specified custom image is used in place of the app icon.

If you’ve set a custom alert icon, you can clear it by setting this property’s value to `nil`, which restores use of the app icon for the alert.

> **Note**: AppKit may omit the icon from the alert if it’s the app icon and the alert’s context is clear, such as being presented as a sheet on an app window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/icon)*