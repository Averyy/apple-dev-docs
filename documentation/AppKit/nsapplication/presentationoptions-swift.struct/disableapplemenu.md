# disableAppleMenu

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

All Apple Menu items are disabled.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static var disableAppleMenu: NSApplication.PresentationOptions { get }
```

```c
NSApplicationPresentationDisableAppleMenu
```

## See Also

### Presentation Options
- [static var autoHideDock: NSApplication.PresentationOptions](./autohidedock.md)
  The dock is normally hidden, but automatically appears when moused near.
- [static var hideDock: NSApplication.PresentationOptions](./hidedock.md)
  The dock is entirely hidden and disabled.
- [static var autoHideMenuBar: NSApplication.PresentationOptions](./autohidemenubar.md)
  The menu bar is normally hidden, but automatically appears when moused near.
- [static var hideMenuBar: NSApplication.PresentationOptions](./hidemenubar.md)
  The menu bar is entirely hidden and disabled.
- [static var disableProcessSwitching: NSApplication.PresentationOptions](./disableprocessswitching.md)
  The process switching user interface (Command + Tab to cycle through apps) is disabled.
- [static var disableForceQuit: NSApplication.PresentationOptions](./disableforcequit.md)
  The force quit panel (displayed by pressing Command + Option + Esc) is disabled
- [static var disableSessionTermination: NSApplication.PresentationOptions](./disablesessiontermination.md)
  The panel that shows the Restart, Shut Down, and Log Out options that are displayed as a result of pushing the power key is disabled.
- [static var disableHideApplication: NSApplication.PresentationOptions](./disablehideapplication.md)
  The app’s “Hide” menu item is disabled.
- [static var disableMenuBarTransparency: NSApplication.PresentationOptions](./disablemenubartransparency.md)
  The menu bar transparency appearance is disabled.
- [static var fullScreen: NSApplication.PresentationOptions](./fullscreen.md)
  The app is in fullscreen mode.
- [static var autoHideToolbar: NSApplication.PresentationOptions](./autohidetoolbar.md)
  When in fullscreen mode the window toolbar is detached from window and hides and shows with autoHidden menuBar.
- [static var disableCursorLocationAssistance: NSApplication.PresentationOptions](./disablecursorlocationassistance.md)
  The behavior that allows the user to shake the mouse to locate the cursor is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/presentationoptions-swift.struct/disableapplemenu)*