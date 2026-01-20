# init(coder:device:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Creates a Euclidean distance transform that uses a specified decoder for your data and runs on a specified device.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
init?(coder aDecoder: NSCoder, device: any MTLDevice)
```

#### Discussion

Use this initializer to specify the location of your data; otherwise, the framework may guess incorrectly.

## Parameters

- `aDecoder`: The decoder for your data.
- `device`: The device that the filter runs on.

## See Also

- [init(device: any MTLDevice)](mpsimageeuclideandistancetransform/init(device:).md)
  Creates a Euclidean distance transform that runs on a specified device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageeuclideandistancetransform/init(coder:device:))*