# init()

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Initializes a capture screen input that provides media data from the main screen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Discussion

Using this initializer is equivalent to calling [`init(displayID:)`](./init%28displayid%29.md) with the result of the [`CGMainDisplayID()`](../../CoreGraphics/cgmaindisplayid%28%29.md) function.

## See Also

### Initializing a capture screen input
- [init?(displayID: CGDirectDisplayID)](./init%28displayid%29.md)
  Initializes a capture screen input that provides media data from the specified display.
- [+ new](./new.md)
  Creates a capture screen input that provides media data from the main screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/init())*