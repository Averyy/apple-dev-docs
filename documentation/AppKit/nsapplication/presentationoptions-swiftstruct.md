# NSApplication.PresentationOptions

**Framework**: AppKit  
**Kind**: struct

Constants that control the presentation of the app, typically for fullscreen apps such as games or kiosks.

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct PresentationOptions
```

#### Overview

There are restrictions on the combination of presentation options that can be set simultaneously:

- [`autoHideDock`](nsapplication/presentationoptions-swift.struct/autohidedock.md) and [`hideDock`](nsapplication/presentationoptions-swift.struct/hidedock.md) are mutually exclusive: You may specify one or the other, but not both.
- [`autoHideMenuBar`](nsapplication/presentationoptions-swift.struct/autohidemenubar.md) and [`hideMenuBar`](nsapplication/presentationoptions-swift.struct/hidemenubar.md) are mutually exclusive: You may specify one or the other, but not both.
- If you specify [`hideMenuBar`](nsapplication/presentationoptions-swift.struct/hidemenubar.md), it must be accompanied by [`hideDock`](nsapplication/presentationoptions-swift.struct/hidedock.md).
- If you specify [`autoHideMenuBar`](nsapplication/presentationoptions-swift.struct/autohidemenubar.md), it must be accompanied by either [`hideDock`](nsapplication/presentationoptions-swift.struct/hidedock.md) or [`autoHideDock`](nsapplication/presentationoptions-swift.struct/autohidedock.md).
- If you specify any of [`disableProcessSwitching`](nsapplication/presentationoptions-swift.struct/disableprocessswitching.md), [`disableForceQuit`](nsapplication/presentationoptions-swift.struct/disableforcequit.md), [`disableSessionTermination`](nsapplication/presentationoptions-swift.struct/disablesessiontermination.md), or [`disableMenuBarTransparency`](nsapplication/presentationoptions-swift.struct/disablemenubartransparency.md), it must be accompanied by either [`hideDock`](nsapplication/presentationoptions-swift.struct/hidedock.md) or [`autoHideDock`](nsapplication/presentationoptions-swift.struct/autohidedock.md).
- [`autoHideToolbar`](nsapplication/presentationoptions-swift.struct/autohidetoolbar.md) may be used only when both [`fullScreen`](nsapplication/presentationoptions-swift.struct/fullscreen.md) and [`autoHideMenuBar`](nsapplication/presentationoptions-swift.struct/autohidemenubar.md) are also set.

When [`NSApplication`](nsapplication.md) receives a parameter value that does not conform to these requirements, it raises an [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException).

## Topics

### Presentation Options
- [static var autoHideDock: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/autohidedock.md)
  The dock is normally hidden, but automatically appears when moused near.
- [static var hideDock: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/hidedock.md)
  The dock is entirely hidden and disabled.
- [static var autoHideMenuBar: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/autohidemenubar.md)
  The menu bar is normally hidden, but automatically appears when moused near.
- [static var hideMenuBar: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/hidemenubar.md)
  The menu bar is entirely hidden and disabled.
- [static var disableAppleMenu: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/disableapplemenu.md)
  All Apple Menu items are disabled.
- [static var disableProcessSwitching: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/disableprocessswitching.md)
  The process switching user interface (Command + Tab to cycle through apps) is disabled.
- [static var disableForceQuit: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/disableforcequit.md)
  The force quit panel (displayed by pressing Command + Option + Esc) is disabled
- [static var disableSessionTermination: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/disablesessiontermination.md)
  The panel that shows the Restart, Shut Down, and Log Out options that are displayed as a result of pushing the power key is disabled.
- [static var disableHideApplication: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/disablehideapplication.md)
  The app’s “Hide” menu item is disabled.
- [static var disableMenuBarTransparency: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/disablemenubartransparency.md)
  The menu bar transparency appearance is disabled.
- [static var fullScreen: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/fullscreen.md)
  The app is in fullscreen mode.
- [static var autoHideToolbar: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/autohidetoolbar.md)
  When in fullscreen mode the window toolbar is detached from window and hides and shows with autoHidden menuBar.
- [static var disableCursorLocationAssistance: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.struct/disablecursorlocationassistance.md)
  The behavior that allows the user to shake the mouse to locate the cursor is disabled.
### Initializers
- [init(rawValue: UInt)](nsapplication/presentationoptions-swift.struct/init(rawvalue:).md)
  Initializes a new presentation options structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var appearance: NSAppearance?](nsapplication/appearance.md)
  The appearance associated with the app’s windows.
- [var effectiveAppearance: NSAppearance](nsapplication/effectiveappearance.md)
  The appearance that AppKit uses to draw the app’s interface.
- [var currentSystemPresentationOptions: NSApplication.PresentationOptions](nsapplication/currentsystempresentationoptions.md)
  The set of app presentation options that are currently in effect for the system.
- [var presentationOptions: NSApplication.PresentationOptions](nsapplication/presentationoptions-swift.property.md)
  The presentation options that should be in effect for the system when this app is active.
- [var applicationShouldSuppressHighDynamicRangeContent: Bool](nsapplication/applicationshouldsuppresshighdynamicrangecontent.md)
  A boolean value indicating whether your application should suppress HDR content based on established policy. Built-in AppKit components such as NSImageView will automatically behave correctly with HDR content. You should use this value in conjunction with notifications (`NSApplicationShouldBeginSuppressingHighDynamicRangeContentNotification` and `NSApplicationShouldEndSuppressingHighDynamicRangeContentNotification`) to suppress HDR content in your application when signaled to do so.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/presentationoptions-swift.struct)*