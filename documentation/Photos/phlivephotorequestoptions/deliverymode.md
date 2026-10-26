# deliveryMode

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The requested Live Photo quality and delivery priority.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var deliveryMode: PHImageRequestOptionsDeliveryMode { get set }
```

```objc
@property (nonatomic, assign) PHImageRequestOptionsDeliveryMode deliveryMode;
```

#### Discussion

Use this property to tell Photos to provide a Live Photo quickly (possibly sacrificing image quality), to provide a high-quality Live Photo (possibly sacrificing speed), or to provide both automatically if needed. See [`PHImageRequestOptionsDeliveryMode`](../phimagerequestoptionsdeliverymode.md).

## See Also

### Specifying Image Request Options
- [var version: PHImageRequestOptionsVersion](./version.md)
  The version of the Live Photo to be requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotorequestoptions/deliverymode)*