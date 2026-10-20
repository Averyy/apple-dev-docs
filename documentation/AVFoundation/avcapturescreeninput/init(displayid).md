# init(displayID:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Initializes a capture screen input that provides media data from the specified display.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init?(displayID: CGDirectDisplayID)
```

```objc
- (instancetype) initWithDisplayID:(CGDirectDisplayID) displayID;
```

#### Return Value

A capture screen input initialized to provide media data from a given display. If the display cannot be used (because it is not available on the system, for example), returns `nil`.

## Parameters

- `displayID`: The ID of the display from which to capture video.

  `CGDirectDisplayID` is defined in `<CoreGraphics/CGDirectDisplay.h>`.

## See Also

### Initializing a capture screen input
- [init()](./init%28%29.md)
  Initializes a capture screen input that provides media data from the main screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/init(displayid:))*