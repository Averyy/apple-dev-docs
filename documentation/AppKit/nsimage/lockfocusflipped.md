# lockFocusFlipped(_:)

**Framework**: AppKit  
**Kind**: method

Prepares the image to receive drawing commands using the specified flipped state.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func lockFocusFlipped(_ flipped: Bool)
```

## Parameters

- `flipped`: [`true`](https://developer.apple.com/documentation/Swift/true) if the drawing context should be flipped, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func lockFocus()](nsimage/lockfocus.md)
  Prepares the image to receive drawing commands.
- [func unlockFocus()](nsimage/unlockfocus.md)
  Removes the focus from the image.
- [convenience init(iconRef: IconRef)](nsimage/init(iconref:).md)
  Initializes the image object with a Carbon-style icon resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/lockfocusflipped(_:))*