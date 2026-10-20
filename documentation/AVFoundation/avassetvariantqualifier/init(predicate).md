# init(predicate:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a variant qualifier with a predicate.

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
convenience init(predicate: NSPredicate)
```

```objc
+ (instancetype) assetVariantQualifierWithPredicate:(NSPredicate *) predicate;
```

## Parameters

- `predicate`: A predicate to find a particular asset variant.

## See Also

### Creating a variant qualifier
- [convenience init(variant: AVAssetVariant)](./init%28variant%29.md)
  Creates a variant qualifier with an asset variant.
- [class AVAssetVariant](../avassetvariant.md)
  An object that represents a bit rate variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetvariantqualifier/init(predicate:))*