# CTUnderlineStyle

**Framework**: Core Text  
**Kind**: struct  
**Role**: Structure

Underline style specifiers.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CTUnderlineStyle
```

```c
enum CTUnderlineStyle : int32_t;
```

#### Overview

You can apply these underline style specifiers to the value that you set with the [`kCTUnderlineStyleAttributeName`](./kctunderlinestyleattributename.md) attribute. These specifiers control the underline style Core Text uses when rendering the text to which the attribute applies.

## Topics

### Constants
- [static var single: CTUnderlineStyle](./ctunderlinestyle/single.md)
  A specifier that indicates to draw an underline consisting of a single line.
- [static var thick: CTUnderlineStyle](./ctunderlinestyle/thick.md)
  A specifier that indicates to draw an underline consisting of a thick line.
- [static var double: CTUnderlineStyle](./ctunderlinestyle/double.md)
  A specifier that indicates to draw an underline consisting of a double line.
- [kCTUnderlineStyleNone](./ctunderlinestyle/kctunderlinestylenone.md)
  A specifier that indicates not to draw an underline.
### Initializers
- [init(rawValue: Int32)](./ctunderlinestyle/init%28rawvalue%29.md)
  Creates an underline style structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [String Attribute Name Constants](./string-attribute-name-constants.md)
  These constants represent string attribute names.
- [struct CTUnderlineStyleModifiers](./ctunderlinestylemodifiers.md)
  Underline style modifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctunderlinestyle)*