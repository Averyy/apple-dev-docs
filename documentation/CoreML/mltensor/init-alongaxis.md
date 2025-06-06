# init(_:alongAxis:)

**Framework**: Core ML  
**Kind**: init

Creates a tensor by stacking the given tensors along the specified axis.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(_ elements: some Collection<MLTensor>, alongAxis axis: Int = 0)
```

## Parameters

- `axis`: The axis along which to stack. Negative values wrap around.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(_:alongaxis:))*