# unlockFocus()

**Framework**: AppKit  
**Kind**: method

Removes the focus from the image.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func unlockFocus()
```

#### Discussion

This message must be sent after a successful [`lockFocus()`](nsimage/lockfocus().md) or [`lockFocusOnRepresentation:`](nsimage/lockfocusonrepresentation:.md) message and the completion of any intermediate drawing commands. This method restores the focus to the previous owner, if any.

Do not send this message if the preceding call to lock focus raised an `NSImageCacheException`.

## See Also

- [func lockFocus()](nsimage/lockfocus.md)
  Prepares the image to receive drawing commands.
- [func lockFocusFlipped(Bool)](nsimage/lockfocusflipped(_:).md)
  Prepares the image to receive drawing commands using the specified flipped state.
- [convenience init(iconRef: IconRef)](nsimage/init(iconref:).md)
  Initializes the image object with a Carbon-style icon resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/unlockfocus())*