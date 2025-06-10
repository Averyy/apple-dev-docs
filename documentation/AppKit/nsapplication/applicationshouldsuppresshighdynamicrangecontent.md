# applicationShouldSuppressHighDynamicRangeContent

**Framework**: AppKit  
**Kind**: property

A boolean value indicating whether your application should suppress HDR content based on established policy. Built-in AppKit components such as NSImageView will automatically behave correctly with HDR content. You should use this value in conjunction with notifications (`NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification` and `NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification`) to suppress HDR content in your application when signaled to do so.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var applicationShouldSuppressHighDynamicRangeContent: Bool { get }
```

## See Also

- [var appearance: NSAppearance?](nsapplication/appearance.md)
  The appearance associated with the app’s windows.
- [var effectiveAppearance: NSAppearance](nsapplication/effectiveappearance.md)
  The appearance that AppKit uses to draw the app’s interface.
- [var currentSystemPresentationOptions: NSApplication.PresentationOptions](nsapplication/currentsystempresentationoptions.md)
  The set of app presentation options that are currently in effect for the system.
- [var presentationOptions: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.property.md)
  The presentation options that should be in effect for the system when this app is active.
- [NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct.md)
  Constants that control the presentation of the app, typically for fullscreen apps such as games or kiosks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/applicationshouldsuppresshighdynamicrangecontent)*