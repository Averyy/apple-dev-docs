# version

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The version of the Live Photo to be requested.

**Availability**:
- iOS 9.1+
- iPadOS 9.1+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var version: PHImageRequestOptionsVersion { get set }
```

```objc
@property (nonatomic, assign) PHImageRequestOptionsVersion version;
```

#### Discussion

Use this property to request a version of the Live Photo with or without adjustments. See [`PHImageRequestOptionsVersion`](../phimagerequestoptionsversion.md).

## See Also

### Specifying Image Request Options
- [var deliveryMode: PHImageRequestOptionsDeliveryMode](./deliverymode.md)
  The requested Live Photo quality and delivery priority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phlivephotorequestoptions/version)*