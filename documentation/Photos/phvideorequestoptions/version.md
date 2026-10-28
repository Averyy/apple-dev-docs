# version

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The version of the video to request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var version: PHVideoRequestOptionsVersion { get set }
```

```objc
@property (nonatomic, assign) PHVideoRequestOptionsVersion version;
```

## Discussion

If a video asset has been edited, use this property to request a video with or without adjustments.

The default option is [`PHVideoRequestOptionsVersion.current`](../phvideorequestoptionsversion/current.md). See [`PHVideoRequestOptionsVersion`](../phvideorequestoptionsversion.md).

## See Also

### Specifying Video Request Options
- [enum PHVideoRequestOptionsVersion](../phvideorequestoptionsversion.md)
  Options for requesting a video asset with or without adjustments, used by the [`version`](./version.md) property.
- [var deliveryMode: PHVideoRequestOptionsDeliveryMode](./deliverymode.md)
  A mode specifying the requested video quality and delivery priority.
- [enum PHVideoRequestOptionsDeliveryMode](../phvideorequestoptionsdeliverymode.md)
  Options for delivering requested video data, used by the [`deliveryMode`](./deliverymode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phvideorequestoptions/version)*