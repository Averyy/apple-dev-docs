# init()

**Framework**: AVFoundation  
**Kind**: init

Initializes a capture screen input that provides media data from the main screen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init()
```

#### Discussion

Using this initializer is equivalent to calling [`init(displayID:)`](avcapturescreeninput/init(displayid:).md) with the result of the [`CGMainDisplayID()`](https://developer.apple.com/documentation/CoreGraphics/CGMainDisplayID()) function.

## See Also

- [init?(displayID: CGDirectDisplayID)](avcapturescreeninput/init(displayid:).md)
  Initializes a capture screen input that provides media data from the specified display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/init())*