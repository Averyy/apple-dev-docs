# UIFont.Weight

**Framework**: Uikit  
**Kind**: struct

Constants that represent standard typeface styles.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 4.0+

## Declaration

```swift
struct Weight
```

#### Overview

Use system-defined constants as interchangeable values for [`weight`](uifontdescriptor/traitkey/weight.md). Each constant corresponds to a different value that indicates the weight of a font. Use these constants to specify the weight parameter in [`systemFont(ofSize:weight:)`](uifont/systemfont(ofsize:weight:).md). When providing a weight that doesn’t precisely match a font face in the family, the system locates a face that most closely matches the request.

> **Note**:  Font [`familyNames`](uifont/familynames.md) don’t include all system-defined font constants.

## Topics

### Using system-defined font weights
- [static let ultraLight: UIFont.Weight](uifont/weight/ultralight.md)
  The ultra-light font weight.
- [static let thin: UIFont.Weight](uifont/weight/thin.md)
  The thin font weight.
- [static let light: UIFont.Weight](uifont/weight/light.md)
  The light font weight.
- [static let regular: UIFont.Weight](uifont/weight/regular.md)
  The regular font weight.
- [static let medium: UIFont.Weight](uifont/weight/medium.md)
  The medium font weight.
- [static let semibold: UIFont.Weight](uifont/weight/semibold.md)
  The semibold font weight.
- [static let bold: UIFont.Weight](uifont/weight/bold.md)
  The bold font weight.
- [static let heavy: UIFont.Weight](uifont/weight/heavy.md)
  The heavy font weight.
- [static let black: UIFont.Weight](uifont/weight/black.md)
  The black font weight.
### Balancing the appearance of symbols and text
- [func symbolWeight() -> UIImage.SymbolWeight](uifont/weight/symbolweight.md)
  Provides the corresponding symbol weight for this font weight.
### Initializers
- [init(CGFloat)](uifont/weight/init(_:).md)
  Creates a font weight.
- [init(rawValue: CGFloat)](uifont/weight/init(rawvalue:).md)
  Creates a font weight with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func systemFont(ofSize: CGFloat) -> UIFont](uifont/systemfont(ofsize:).md)
  Returns the font object for standard interface items in the specified size.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/systemfont(ofsize:weight:).md)
  Returns the font object for standard interface items in the specified size and weight.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight, width: UIFont.Width) -> UIFont](uifont/systemfont(ofsize:weight:width:).md)
- [UIFont.Width](uifont/width.md)
- [class func boldSystemFont(ofSize: CGFloat) -> UIFont](uifont/boldsystemfont(ofsize:).md)
  Returns the font object for standard interface items in boldface type in the specified size.
- [class func italicSystemFont(ofSize: CGFloat) -> UIFont](uifont/italicsystemfont(ofsize:).md)
  Returns the font object for standard interface items in italic type in the specified size.
- [class func monospacedSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/monospacedsystemfont(ofsize:weight:).md)
  Returns the fixed-width font for standard interface text in the specified size.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/monospaceddigitsystemfont(ofsize:weight:).md)
  Returns the standard system font with all digits of consistent width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/weight)*