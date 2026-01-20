# init(device:kernelSize:)

**Framework**: Metal Performance Shaders  
**Kind**: init

Initializes a normalization kernel in a channel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, kernelSize: Int)
```

#### Return Value

A valid [`MPSCNNCrossChannelNormalization`](mpscnncrosschannelnormalization.md) object or `nil`, if failure.

## Parameters

- `device`: The device the filter will run on.
- `kernelSize`: The size of the kernel, in both x and y dimensions.

## See Also

- [init?(coder: NSCoder, device: any MTLDevice)](mpscnncrosschannelnormalization/init(coder:device:).md)
  Initializes a normalization kernel in a channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnncrosschannelnormalization/init(device:kernelsize:))*