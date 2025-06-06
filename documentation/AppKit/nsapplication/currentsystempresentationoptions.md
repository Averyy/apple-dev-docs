# currentSystemPresentationOptions

**Framework**: AppKit  
**Kind**: property

The set of app presentation options that are currently in effect for the system.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var currentSystemPresentationOptions: NSApplication.PresentationOptions { get }
```

#### Return Value

The presentation options. The constants are listed in [`NSApplication.PresentationOptions`](nsapplication/presentationoptions-swift.struct.md) and can combined using a C bitwise OR operator.

#### Discussion

This property contains the presentation options that have been put into effect by the currently active app. You can use key-value observing on this property to receive notifications when:

- The client is the active app and makes a change itself using either the [`presentationOptions`](nsapplication/presentationoptions-swift.property.md) property or the `SetSystemUIMode` function.
- Another app is active and makes presentation changes of its own.
- Another app becomes active and causes the active set of presentation options to change.

Key-value observing notifications aren’t sent when one of the above conditions occur, but has the same set of presentation options as the previously active app.

## See Also

- [var appearance: NSAppearance?](nsapplication/appearance.md)
  The appearance associated with the app’s windows.
- [var effectiveAppearance: NSAppearance](nsapplication/effectiveappearance.md)
  The appearance that AppKit uses to draw the app’s interface.
- [var presentationOptions: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.property.md)
  The presentation options that should be in effect for the system when this app is active.
- [NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct.md)
  Constants that control the presentation of the app, typically for fullscreen apps such as games or kiosks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/currentsystempresentationoptions)*