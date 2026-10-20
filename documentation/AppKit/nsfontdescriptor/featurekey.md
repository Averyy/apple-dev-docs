# NSFontDescriptor.FeatureKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants to use as keys to retrieve information about a font descriptor from its feature dictionary.

**Availability**:
- macOS

## Declaration

```swift
struct FeatureKey
```

```c
typedef NSString * NSFontDescriptorFeatureKey;
```

#### Discussion

These keys are used with [`featureSettings`](./attributename/featuresettings.md).

## Topics

### Feature Keys
- [static let typeIdentifier: NSFontDescriptor.FeatureKey](./featurekey/typeidentifier.md)
  A key that indicates the type of the font feature.
- [static let selectorIdentifier: NSFontDescriptor.FeatureKey](./featurekey/selectoridentifier.md)
  A key that indicates the selector of the font feature.
### Initializers
- [init(String)](./featurekey/init%28_%29.md)
- [init(rawValue: String)](./featurekey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Font Attributes
- [var fontAttributes: [NSFontDescriptor.AttributeName : Any]](./fontattributes.md)
  The receiver’s dictionary of attributes.
- [func object(forKey: NSFontDescriptor.AttributeName) -> Any?](./object%28forkey%29.md)
  Returns the font attribute specified by the given key.
- [NSFontDescriptor.AttributeName](./attributename.md)
  Constants for the names of font attributes.
- [NSFontDescriptor.SymbolicTraits](./symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [var matrix: AffineTransform?](./matrix.md)
  The current transform matrix of the receiver.
- [var pointSize: CGFloat](./pointsize.md)
  The point size of the receiver.
- [var postscriptName: String?](./postscriptname.md)
  The PostScript name of the receiver.
- [typealias NSFontFamilyClass](../nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [var NSFontFamilyClassMask: UInt32](../nsfontfamilyclassmask.md)
  Constant you use to access `NSFontFamilyClass` values in the upper four bits of `NSFontSymbolicTraits`.
- [Typeface Information](../typeface-information.md)
  Constants for type faces such as italic or bold.
- [NSFontDescriptor.VariationKey](./variationkey.md)
  Constants that can be used as keys to retrieve information about a font descriptor from its variation axis dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/featurekey)*