# applicationShouldSuppressHighDynamicRangeContent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A boolean value indicating whether your application should suppress HDR content based on established policy. Built-in AppKit components such as NSImageView will automatically behave correctly with HDR content. You should use this value in conjunction with notifications (`NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification` and `NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification`) to suppress HDR content in your application when signaled to do so.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var applicationShouldSuppressHighDynamicRangeContent: Bool { get }
```

```objc
@property (readonly) BOOL applicationShouldSuppressHighDynamicRangeContent;
```

## See Also

### Managing the app’s appearance
- [var appearance: NSAppearance?](./appearance.md)
  The appearance associated with the app’s windows.
- [var effectiveAppearance: NSAppearance](./effectiveappearance.md)
  The appearance that AppKit uses to draw the app’s interface.
- [var currentSystemPresentationOptions: NSApplication.PresentationOptions](./currentsystempresentationoptions.md)
  The set of app presentation options that are currently in effect for the system.
- [var presentationOptions: NSApplication.PresentationOptions](./presentationoptions-swift.property.md)
  The presentation options that should be in effect for the system when this app is active.
- [NSApplication.PresentationOptions](./presentationoptions-swift.struct.md)
  Constants that control the presentation of the app, typically for fullscreen apps such as games or kiosks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/applicationshouldsuppresshighdynamicrangecontent)*