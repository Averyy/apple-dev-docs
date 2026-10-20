# init(device:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Creates a Euclidean distance transform that runs on a specified device.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device;
```

## Parameters

- `device`: The device that the filter runs on.

## See Also

### Creating a Euclidean distance transform
- [init?(coder: NSCoder, device: any MTLDevice)](./init%28coder,device%29.md)
  Creates a Euclidean distance transform that uses a specified decoder for your data and runs on a specified device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageeuclideandistancetransform/init(device:))*