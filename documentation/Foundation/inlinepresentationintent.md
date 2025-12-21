# InlinePresentationIntent

**Framework**: Foundation  
**Kind**: struct

A type that defines presentation intent for runs of characters for traits like emphasis, strikethrough, and code voice.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct InlinePresentationIntent
```

## Topics

### Getting inline presentation types
- [static var code: InlinePresentationIntent](inlinepresentationintent/code.md)
  An intent that represents a code voice presentation.
- [static var emphasized: InlinePresentationIntent](inlinepresentationintent/emphasized.md)
  An intent that represents an emphasized presentation.
- [static var lineBreak: InlinePresentationIntent](inlinepresentationintent/linebreak.md)
  An intent that represents a line break.
- [static var softBreak: InlinePresentationIntent](inlinepresentationintent/softbreak.md)
  An intent that represents a soft line break.
- [static var strikethrough: InlinePresentationIntent](inlinepresentationintent/strikethrough.md)
  An intent that represents a strikethrough presentation.
- [static var stronglyEmphasized: InlinePresentationIntent](inlinepresentationintent/stronglyemphasized.md)
  An intent that represents a strongly emphasized presentation.
- [static var inlineHTML: InlinePresentationIntent](inlinepresentationintent/inlinehtml.md)
  An intent that represents an inline HTML presentation.
- [static var blockHTML: InlinePresentationIntent](inlinepresentationintent/blockhtml.md)
  An intent that represents a block HTML presentation.
### Initializers
- [init(rawValue: UInt)](inlinepresentationintent/init(rawvalue:).md)
  Creates an inline presentation intent using the raw value you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/inlinepresentationintent)*