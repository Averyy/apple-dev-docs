# CTUnderlineStyle

**Framework**: Core Text  
**Kind**: struct

Underline style specifiers.

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
struct CTUnderlineStyle
```

#### Overview

You can apply these underline style specifiers to the value that you set with the [`kCTUnderlineStyleAttributeName`](kctunderlinestyleattributename.md) attribute. These specifiers control the underline style Core Text uses when rendering the text to which the attribute applies.

## Topics

### Constants
- [static var single: CTUnderlineStyle](ctunderlinestyle/single.md)
  A specifier that indicates to draw an underline consisting of a single line.
- [static var thick: CTUnderlineStyle](ctunderlinestyle/thick.md)
  A specifier that indicates to draw an underline consisting of a thick line.
- [static var double: CTUnderlineStyle](ctunderlinestyle/double.md)
  A specifier that indicates to draw an underline consisting of a double line.
### Initializers
- [init(rawValue: Int32)](ctunderlinestyle/init(rawvalue:).md)
  Creates an underline style structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [String Attribute Name Constants](string-attribute-name-constants.md)
  These constants represent string attribute names.
- [struct CTUnderlineStyleModifiers](ctunderlinestylemodifiers.md)
  Underline style modifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctunderlinestyle)*