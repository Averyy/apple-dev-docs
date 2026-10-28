# preferredMetalDevice

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readwrite, nullable) id<MTLDevice> preferredMetalDevice;
```

## Discussion

If [`preferredMetalDevice`](./preferredmetaldevice.md) is `nil`, the default value, Core ML chooses a metal device for you.

## See Also

### Configuring GPU usage
- [var allowLowPrecisionAccumulationOnGPU: Bool](./allowlowprecisionaccumulationongpu.md)
  A Boolean value that determines whether to allow low-precision accumulation on a GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelconfiguration/preferredmetaldevice)*