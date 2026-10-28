# presentationOptions

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The presentation options that should be in effect for the system when this app is active.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var presentationOptions: NSApplication.PresentationOptions { get set }
```

```objc
@property NSApplicationPresentationOptions presentationOptions;
```

## Discussion

This value contains a bitwise OR of the constants listed in [`NSApplication.PresentationOptions`](./presentationoptions-swift.struct.md). Trying to set the property to an invalid combination of option flags raises an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception. See the constants for a description of the valid combinations.

## See Also

### Managing the app’s appearance
- [var appearance: NSAppearance?](./appearance.md)
  The appearance associated with the app’s windows.
- [var effectiveAppearance: NSAppearance](./effectiveappearance.md)
  The appearance that AppKit uses to draw the app’s interface.
- [var currentSystemPresentationOptions: NSApplication.PresentationOptions](./currentsystempresentationoptions.md)
  The set of app presentation options that are currently in effect for the system.
- [NSApplication.PresentationOptions](./presentationoptions-swift.struct.md)
  Constants that control the presentation of the app, typically for fullscreen apps such as games or kiosks.
- [var applicationShouldSuppressHighDynamicRangeContent: Bool](./applicationshouldsuppresshighdynamicrangecontent.md)
  A boolean value indicating whether your application should suppress HDR content based on established policy. Built-in AppKit components such as NSImageView will automatically behave correctly with HDR content. You should use this value in conjunction with notifications (`NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification` and `NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification`) to suppress HDR content in your application when signaled to do so.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/presentationoptions-swift.property)*