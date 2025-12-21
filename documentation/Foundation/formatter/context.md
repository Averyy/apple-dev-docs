# Formatter.Context

**Framework**: Foundation  
**Kind**: enum

The formatting context for a formatter.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum Context
```

#### Overview

Use formatting contexts to specify where the result of formatting will appear, so that the formatter can provide the most appropriate result.

For example, when formatting a date or date symbol for a French locale, you want the month name to be capitalized if it appears at the beginning of the sentence (“Juin est mon mois de naissance”), but not if it appears elsewhere (“Mon mois de naissance est juin”).

If the formatting context isn’t known ahead of time, specify [`Formatter.Context.dynamic`](formatter/context/dynamic.md) to have the system determine the context automatically.

## Topics

### Constants
- [Formatter.Context.unknown](formatter/context/unknown.md)
  An unknown formatting context.
- [Formatter.Context.dynamic](formatter/context/dynamic.md)
  A formatting context determined automatically at runtime.
- [Formatter.Context.standalone](formatter/context/standalone.md)
  The formatting context for stand-alone usage.
- [Formatter.Context.listItem](formatter/context/listitem.md)
  The formatting context for a list or menu item.
- [Formatter.Context.beginningOfSentence](formatter/context/beginningofsentence.md)
  The formatting context for the beginning of a sentence.
- [Formatter.Context.middleOfSentence](formatter/context/middleofsentence.md)
  The formatting context for the middle of a sentence.
### Initializers
- [init?(rawValue: Int)](formatter/context/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Formatter.UnitStyle](formatter/unitstyle.md)
  Specifies the width of the unit, determining the textual representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter/context)*