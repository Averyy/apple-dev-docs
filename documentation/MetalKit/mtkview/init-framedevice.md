# init(frame:device:)

**Framework**: MetalKit  
**Kind**: init

Initializes a view with the specified frame rectangle and Metal device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(frame frameRect: CGRect, device: (any MTLDevice)?)
```

#### Return Value

An initialized view object.

## Parameters

- `frameRect`: The frame rectangle for the view.
- `device`: The Metal device object to use.

## See Also

- [init(coder: NSCoder)](mtkview/init(coder:).md)
  Initializes a view from data in a given unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkview/init(frame:device:))*