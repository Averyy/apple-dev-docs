# deliveryMode

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A mode specifying the requested video quality and delivery priority.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var deliveryMode: PHVideoRequestOptionsDeliveryMode { get set }
```

```objc
@property (nonatomic, assign) PHVideoRequestOptionsDeliveryMode deliveryMode;
```

## Discussion

Use this property to tell Photos to provide a video quickly (possibly sacrificing image quality) or to provide a high-quality video (possibly sacrificing speed). This option applies only when requesting the current version of the video (that is, only when the [`version`](./version.md) property is [`PHVideoRequestOptionsVersion.current`](../phvideorequestoptionsversion/current.md)).

The default option is [`PHVideoRequestOptionsDeliveryMode.automatic`](../phvideorequestoptionsdeliverymode/automatic.md). See [`PHVideoRequestOptionsDeliveryMode`](../phvideorequestoptionsdeliverymode.md).

## See Also

### Specifying Video Request Options
- [var version: PHVideoRequestOptionsVersion](./version.md)
  The version of the video to request.
- [enum PHVideoRequestOptionsVersion](../phvideorequestoptionsversion.md)
  Options for requesting a video asset with or without adjustments, used by the [`version`](./version.md) property.
- [enum PHVideoRequestOptionsDeliveryMode](../phvideorequestoptionsdeliverymode.md)
  Options for delivering requested video data, used by the [`deliveryMode`](./deliverymode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phvideorequestoptions/deliverymode)*