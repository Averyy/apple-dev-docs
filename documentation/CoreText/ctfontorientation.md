# CTFontOrientation

**Framework**: Core Text  
**Kind**: enum

The intended rendering orientation of the font for obtaining glyph metrics.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CTFontOrientation
```

#### Overview

Use the values of this enumeration for [`kCTFontOrientationAttribute`](kctfontorientationattribute.md).

## Topics

### Font Orientations
- [CTFontOrientation.default](ctfontorientation/default.md)
  The native orientation of the font.
- [CTFontOrientation.horizontal](ctfontorientation/horizontal.md)
  The horizontal orientation.
- [CTFontOrientation.vertical](ctfontorientation/vertical.md)
  The vertical orientation.
### Deprecated Constants
- [static var kCTFontDefaultOrientation: CTFontOrientation](ctfontorientation/kctfontdefaultorientation.md)
  The native orientation of the font.
- [static var kCTFontHorizontalOrientation: CTFontOrientation](ctfontorientation/kctfonthorizontalorientation.md)
  The horizontal orientation.
- [static var kCTFontVerticalOrientation: CTFontOrientation](ctfontorientation/kctfontverticalorientation.md)
  The vertical orientation.
### Initializers
- [init?(rawValue: UInt32)](ctfontorientation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let kCTFontOrientationAttribute: CFString](kctfontorientationattribute.md)
  The orientation for the glyphs of the font.
- [Font Attributes](font-attributes.md)
  The keys for accessing font attributes from a font descriptor.
- [enum CTFontFormat](ctfontformat.md)
  The recognized format of the font.
- [typealias CTFontPriority](ctfontpriority.md)
  The priority of font descriptors when resolving duplicates and sorting match results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontorientation)*