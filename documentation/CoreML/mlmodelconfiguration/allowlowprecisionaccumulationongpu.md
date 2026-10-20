# allowLowPrecisionAccumulationOnGPU

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether to allow low-precision accumulation on a GPU.

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
var allowLowPrecisionAccumulationOnGPU: Bool { get set }
```

```objc
@property (readwrite) BOOL allowLowPrecisionAccumulationOnGPU;
```

## See Also

### Configuring GPU usage
- [var preferredMetalDevice: (any MTLDevice)?](./preferredmetaldevice.md)
  The metal device you prefer this model use to make predictions (inference) and update the model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelconfiguration/allowlowprecisionaccumulationongpu)*