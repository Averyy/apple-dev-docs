# deepest

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns a screen object representing the screen that can best represent color.

**Availability**:
- macOS

## Declaration

```swift
class var deepest: NSScreen? { get }
```

```objc
@property (class, strong, readonly, nullable) NSScreen * deepestScreen;
```

## Return Value

The screen with the highest bit depth.

## Discussion

This method always returns an object, even if there is only one screen and it is not a color screen.

## See Also

### Getting Screen Objects
- [class var main: NSScreen?](./main.md)
  Returns the screen object containing the window with the keyboard focus.
- [class var screens: [NSScreen]](./screens.md)
  Returns an array of screen objects representing all of the screens available on the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/deepest)*