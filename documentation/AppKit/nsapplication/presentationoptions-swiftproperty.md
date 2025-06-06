# presentationOptions

**Framework**: AppKit  
**Kind**: property

The presentation options that should be in effect for the system when this app is active.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var presentationOptions: NSApplication.PresentationOptions { get set }
```

#### Discussion

This value contains a bitwise OR of the constants listed in [`NSApplication.PresentationOptions`](nsapplication/presentationoptions-swift.struct.md). Trying to set the property to an invalid combination of option flags raises an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) exception. See the constants for a description of the valid combinations.

## See Also

- [var appearance: NSAppearance?](nsapplication/appearance.md)
  The appearance associated with the app’s windows.
- [var effectiveAppearance: NSAppearance](nsapplication/effectiveappearance.md)
  The appearance that AppKit uses to draw the app’s interface.
- [var currentSystemPresentationOptions: NSApplication.PresentationOptions](nsapplication/currentsystempresentationoptions.md)
  The set of app presentation options that are currently in effect for the system.
- [NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct.md)
  Constants that control the presentation of the app, typically for fullscreen apps such as games or kiosks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/presentationoptions-swift.property)*