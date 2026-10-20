# UIFont.Weight

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that represent standard typeface styles.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 4.0+

## Declaration

```swift
struct Weight
```

```c
typedef CGFloat UIFontWeight;
```

#### Overview

Use system-defined constants as interchangeable values for [`weight`](../uifontdescriptor/traitkey/weight.md). Each constant corresponds to a different value that indicates the weight of a font. Use these constants to specify the weight parameter in [`systemFont(ofSize:weight:)`](./systemfont%28ofsize,weight%29.md). When providing a weight that doesn’t precisely match a font face in the family, the system locates a face that most closely matches the request.

> **Note**:  Font [`familyNames`](./familynames.md) don’t include all system-defined font constants.

## Topics

### Using system-defined font weights
- [static let ultraLight: UIFont.Weight](./weight/ultralight.md)
  The ultra-light font weight.
- [static let thin: UIFont.Weight](./weight/thin.md)
  The thin font weight.
- [static let light: UIFont.Weight](./weight/light.md)
  The light font weight.
- [static let regular: UIFont.Weight](./weight/regular.md)
  The regular font weight.
- [static let medium: UIFont.Weight](./weight/medium.md)
  The medium font weight.
- [static let semibold: UIFont.Weight](./weight/semibold.md)
  The semibold font weight.
- [static let bold: UIFont.Weight](./weight/bold.md)
  The bold font weight.
- [static let heavy: UIFont.Weight](./weight/heavy.md)
  The heavy font weight.
- [static let black: UIFont.Weight](./weight/black.md)
  The black font weight.
### Balancing the appearance of symbols and text
- [func symbolWeight() -> UIImage.SymbolWeight](./weight/symbolweight%28%29.md)
  Provides the corresponding symbol weight for this font weight.
### Initializers
- [init(CGFloat)](./weight/init%28_%29.md)
  Creates a font weight.
- [init(rawValue: CGFloat)](./weight/init%28rawvalue%29.md)
  Creates a font weight with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating System Fonts
- [class func systemFont(ofSize: CGFloat) -> UIFont](./systemfont%28ofsize%29.md)
  Returns the font object for standard interface items in the specified size.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](./systemfont%28ofsize,weight%29.md)
  Returns the font object for standard interface items in the specified size and weight.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight, width: UIFont.Width) -> UIFont](./systemfont%28ofsize,weight,width%29.md)
- [UIFont.Width](./width.md)
- [class func boldSystemFont(ofSize: CGFloat) -> UIFont](./boldsystemfont%28ofsize%29.md)
  Returns the font object for standard interface items in boldface type in the specified size.
- [class func italicSystemFont(ofSize: CGFloat) -> UIFont](./italicsystemfont%28ofsize%29.md)
  Returns the font object for standard interface items in italic type in the specified size.
- [class func monospacedSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](./monospacedsystemfont%28ofsize,weight%29.md)
  Returns the fixed-width font for standard interface text in the specified size.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](./monospaceddigitsystemfont%28ofsize,weight%29.md)
  Returns the standard system font with all digits of consistent width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/weight)*