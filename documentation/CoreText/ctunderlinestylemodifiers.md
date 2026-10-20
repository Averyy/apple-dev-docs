# CTUnderlineStyleModifiers

**Framework**: Core Text  
**Kind**: struct  
**Role**: Structure

Underline style modifiers.

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
struct CTUnderlineStyleModifiers
```

```c
enum CTUnderlineStyleModifiers : int32_t;
```

#### Overview

You can apply these underline style modifiers to the underline style ([`CTUnderlineStyle`](./ctunderlinestyle.md)) that you set with the [`kCTUnderlineStyleAttributeName`](./kctunderlinestyleattributename.md) attribute. These modifiers control the pattern of the underline.

## Topics

### Constants
- [static var patternSolid: CTUnderlineStyleModifiers](./ctunderlinestylemodifiers/patternsolid.md)
  A modifier that indicates to draw a solid underline.
- [static var patternDot: CTUnderlineStyleModifiers](./ctunderlinestylemodifiers/patterndot.md)
  A modifier that indicates to draw an underline using a pattern of dots.
- [static var patternDash: CTUnderlineStyleModifiers](./ctunderlinestylemodifiers/patterndash.md)
  A modifier that indicates to draw an underline using a pattern of dashes.
- [static var patternDashDot: CTUnderlineStyleModifiers](./ctunderlinestylemodifiers/patterndashdot.md)
  A modifier that indicates to draw an underline using a pattern of alternating dashes and dots.
- [static var patternDashDotDot: CTUnderlineStyleModifiers](./ctunderlinestylemodifiers/patterndashdotdot.md)
  A modifier that indicates to draw an underline using a pattern of a dash followed by two dots.
### Initializers
- [init(rawValue: Int32)](./ctunderlinestylemodifiers/init%28rawvalue%29.md)
  Creates an underline style modifiers structure with the specified raw value.

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
- [struct CTUnderlineStyle](./ctunderlinestyle.md)
  Underline style specifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctunderlinestylemodifiers)*