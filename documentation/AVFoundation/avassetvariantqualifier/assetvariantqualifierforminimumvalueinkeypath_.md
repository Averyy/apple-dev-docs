# assetVariantQualifierForMinimumValueInKeyPath:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a qualifer for finding variant with minimum value in the input key path.

## Declaration

```objc
+ (instancetype) assetVariantQualifierForMinimumValueInKeyPath:(NSString *) keyPath;
```

## Parameters

- `keyPath`: AVAssetVariant keyPath. Allowed keyPath values are peakBitRate, averageBitRate, videoAttributes.presentationSize. Must be a valid, non-nil NSString.

## See Also

### Creating a variant qualifier
- [convenience init(variant: AVAssetVariant)](./init%28variant%29.md)
  Creates a variant qualifier with an asset variant.
- [class AVAssetVariant](../avassetvariant.md)
  An object that represents a bit rate variant.
- [convenience init(predicate: NSPredicate)](./init%28predicate%29.md)
  Creates a variant qualifier with a predicate.
- [+ assetVariantQualifierForMaximumValueInKeyPath:](./assetvariantqualifierformaximumvalueinkeypath_.md)
  Returns a qualifer for finding variant with maximum value in the input key path


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/assetvariantqualifierforminimumvalueinkeypath:)*