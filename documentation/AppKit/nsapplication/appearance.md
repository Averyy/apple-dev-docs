# appearance

**Framework**: AppKit  
**Kind**: property

The appearance associated with the app’s windows.

**Availability**:
- macOS 10.14+

## Declaration

```swift
@MainActor
var appearance: NSAppearance? { get set }
```

## Mentions

- [Choosing a Specific Appearance for Your macOS App](choosing-a-specific-appearance-for-your-macos-app.md)

#### Discussion

When the value of this property is `nil` (the default), AppKit applies the current system appearance to the app’s user interface elements, including its windows, views, panels, and popovers. Assigning an [`NSAppearance`](nsappearance.md) object to this property causes the app’s interface elements to adopt the specified appearance instead.

Individual windows and views may still override the app’s appearance to customize their own appearance.

## See Also

- [var effectiveAppearance: NSAppearance](nsapplication/effectiveappearance.md)
  The appearance that AppKit uses to draw the app’s interface.
- [var currentSystemPresentationOptions: NSApplication.PresentationOptions](nsapplication/currentsystempresentationoptions.md)
  The set of app presentation options that are currently in effect for the system.
- [var presentationOptions: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.property.md)
  The presentation options that should be in effect for the system when this app is active.
- [NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct.md)
  Constants that control the presentation of the app, typically for fullscreen apps such as games or kiosks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/appearance)*