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

This value contains a bitwise OR of the constants listed in [`NSApplication.PresentationOptions`](nsapplication/presentationoptions-swift.struct.md). Trying to set the property to an invalid combination of option flags raises an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) exception. See the constants for a description of the valid combinations.

## See Also

- [var appearance: NSAppearance?](nsapplication/appearance.md)
  The appearance associated with the app’s windows.
- [var effectiveAppearance: NSAppearance](nsapplication/effectiveappearance.md)
  The appearance that AppKit uses to draw the app’s interface.
- [var currentSystemPresentationOptions: NSApplication.PresentationOptions](nsapplication/currentsystempresentationoptions.md)
  The set of app presentation options that are currently in effect for the system.
- [NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct.md)
  Constants that control the presentation of the app, typically for fullscreen apps such as games or kiosks.
- [var applicationShouldSuppressHighDynamicRangeContent: Bool](nsapplication/applicationshouldsuppresshighdynamicrangecontent.md)
  A boolean value indicating whether your application should suppress HDR content based on established policy. Built-in AppKit components such as NSImageView will automatically behave correctly with HDR content. You should use this value in conjunction with notifications (`NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification` and `NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification`) to suppress HDR content in your application when signaled to do so.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/presentationoptions-swift.property)*