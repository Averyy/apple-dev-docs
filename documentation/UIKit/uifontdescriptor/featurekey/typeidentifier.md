# typeIdentifier

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A key for identifying the font feature selector.

**Availability**:
- iOS 7.0+ - Deprecated in 15.0
- iPadOS 7.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- tvOS - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 8.0

> **Deprecated**: Use [`selector`](./selector.md) instead.

## Declaration

```swift
static let typeIdentifier: UIFontDescriptor.FeatureKey
```

```c
extern UIFontDescriptorFeatureKey const UIFontFeatureSelectorIdentifierKey;
```

## Discussion

The value of this key is an [`NSNumber`](../../../Foundation/nsnumber.md) object specifying the ligature, character shape, or other font feature.

## See Also

### Keys
- [static let type: UIFontDescriptor.FeatureKey](./type.md)
  A key for identifying the font feature type.
- [static let selector: UIFontDescriptor.FeatureKey](./selector.md)
  A key for identifying the font feature selector.
- [static let featureIdentifier: UIFontDescriptor.FeatureKey](./featureidentifier.md)
  A key for identifying a font feature type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/featurekey/typeidentifier)*