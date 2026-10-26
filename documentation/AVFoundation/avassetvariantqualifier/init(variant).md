# init(variant:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a variant qualifier with an asset variant.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
convenience init(variant: AVAssetVariant)
```

```objc
+ (instancetype) assetVariantQualifierWithVariant:(AVAssetVariant *) variant;
```

## Parameters

- `variant`: The asset variant for the qualifier.

## See Also

### Creating a variant qualifier
- [class AVAssetVariant](../avassetvariant.md)
  An object that represents a bit rate variant.
- [convenience init(predicate: NSPredicate)](./init%28predicate%29.md)
  Creates a variant qualifier with a predicate.
- [+ assetVariantQualifierForMaximumValueInKeyPath:](./assetvariantqualifierformaximumvalueinkeypath_.md)
  Returns a qualifer for finding variant with maximum value in the input key path
- [+ assetVariantQualifierForMinimumValueInKeyPath:](./assetvariantqualifierforminimumvalueinkeypath_.md)
  Returns a qualifer for finding variant with minimum value in the input key path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/init(variant:))*