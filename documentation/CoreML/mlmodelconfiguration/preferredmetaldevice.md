# preferredMetalDevice

**Framework**: Core ML  
**Kind**: property

The metal device you prefer this model use to make predictions (inference) and update the model.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var preferredMetalDevice: (any MTLDevice)? { get set }
```

#### Discussion

If [`preferredMetalDevice`](mlmodelconfiguration/preferredmetaldevice.md) is `nil`, the default value, Core ML chooses a metal device for you.

## See Also

- [var allowLowPrecisionAccumulationOnGPU: Bool](mlmodelconfiguration/allowlowprecisionaccumulationongpu.md)
  A Boolean value that determines whether to allow low-precision accumulation on a GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelconfiguration/preferredmetaldevice)*