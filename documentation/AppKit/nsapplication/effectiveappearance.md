# effectiveAppearance

**Framework**: AppKit  
**Kind**: property

The appearance that AppKit uses to draw the app’s interface.

**Availability**:
- macOS 10.14+

## Declaration

```swift
@MainActor
var effectiveAppearance: NSAppearance { get }
```

#### Discussion

This property always contains an [`NSAppearance`](nsappearance.md) object representing the appearance to use during drawing. If you don’t explicitly assign a value to the [`appearance`](nsapplication/appearance.md) property, the app inherits the system’s effective appearance.

## See Also

- [var appearance: NSAppearance?](nsapplication/appearance.md)
  The appearance associated with the app’s windows.
- [var currentSystemPresentationOptions: NSApplication.PresentationOptions](nsapplication/currentsystempresentationoptions.md)
  The set of app presentation options that are currently in effect for the system.
- [var presentationOptions: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.property.md)
  The presentation options that should be in effect for the system when this app is active.
- [NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct.md)
  Constants that control the presentation of the app, typically for fullscreen apps such as games or kiosks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/effectiveappearance)*