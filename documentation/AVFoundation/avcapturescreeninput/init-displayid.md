# init(displayID:)

**Framework**: AVFoundation  
**Kind**: init

Initializes a capture screen input that provides media data from the specified display.

**Availability**:
- macOS 10.7+

## Declaration

```swift
init?(displayID: CGDirectDisplayID)
```

#### Return Value

A capture screen input initialized to provide media data from a given display. If the display cannot be used (because it is not available on the system, for example), returns `nil`.

## Parameters

- `displayID`:  is defined in  .

## See Also

- [init()](avcapturescreeninput/init.md)
  Initializes a capture screen input that provides media data from the main screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/init(displayid:))*