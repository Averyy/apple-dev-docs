# selectorIdentifier

**Framework**: AppKit  
**Kind**: property

A key that indicates the selector of the font feature.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static let selectorIdentifier: NSFontDescriptor.FeatureKey
```

#### Discussion

The value of this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object specifying a font feature selector such as common ligature off, traditional character shape, and so on. For more information on Apple Fonts see[` Fonts for Apple platforms`](https://developer.apple.comhttps://developer.apple.com/fonts/) and the [`AAT Font Feature Registry`](https://developer.apple.comhttps://developer.apple.com/fonts/TrueType-Reference-Manual/RM09/AppendixF.html).

## See Also

- [static let typeIdentifier: NSFontDescriptor.FeatureKey](nsfontdescriptor/featurekey/typeidentifier.md)
  A key that indicates the type of the font feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/featurekey/selectoridentifier)*