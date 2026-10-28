# typeIdentifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A key that indicates the type of the font feature.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let typeIdentifier: NSFontDescriptor.FeatureKey
```

```c
extern NSFontDescriptorFeatureKey NSFontFeatureTypeIdentifierKey;
```

## Discussion

The value of this key is an [`NSNumber`](../../../Foundation/nsnumber.md) object specifying a font feature type such as ligature, character shape, and so on. For more information on Apple Fonts see[ Fonts for Apple platforms](https://developer.apple.com/fonts/) and the [AAT Font Feature Registry](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM09/AppendixF.html).

## See Also

### Feature Keys
- [static let selectorIdentifier: NSFontDescriptor.FeatureKey](./selectoridentifier.md)
  A key that indicates the selector of the font feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/featurekey/typeidentifier)*