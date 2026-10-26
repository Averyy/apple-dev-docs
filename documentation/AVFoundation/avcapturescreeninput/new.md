# new

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates a capture screen input that provides media data from the main screen.

**Availability**:
- macOS 10.7+

## Declaration

```objc
+ (instancetype) new;
```

#### Discussion

Using this method is equivalent to calling [`init(displayID:)`](./init%28displayid%29.md) with the result of the [`CGMainDisplayID()`](../../CoreGraphics/cgmaindisplayid%28%29.md) function.

## See Also

### Initializing a capture screen input
- [init?(displayID: CGDirectDisplayID)](./init%28displayid%29.md)
  Initializes a capture screen input that provides media data from the specified display.
- [init()](./init%28%29.md)
  Initializes a capture screen input that provides media data from the main screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/new)*