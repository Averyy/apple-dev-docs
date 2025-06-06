# main

**Framework**: AppKit  
**Kind**: property

Returns the screen object containing the window with the keyboard focus.

**Availability**:
- macOS ?+

## Declaration

```swift
class var main: NSScreen? { get }
```

#### Return Value

The main screen object.

#### Discussion

The main screen is not necessarily the same screen that contains the menu bar or has its origin at `(0, 0)`. The main screen refers to the screen containing the window that is currently receiving keyboard events. It is the main screen because it is the one with which the user is most likely interacting.

The screen containing the menu bar is always the first object (index `0`) in the array returned by the [`screens`](nsscreen/screens.md) method.

## See Also

- [Cocoa Drawing Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)
- [class var deepest: NSScreen?](nsscreen/deepest.md)
  Returns a screen object representing the screen that can best represent color.
- [class var screens: [NSScreen]](nsscreen/screens.md)
  Returns an array of screen objects representing all of the screens available on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/main)*