# Formatter.Context

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NSFormattingContext : NSInteger;
```

## Overview

Use formatting contexts to specify where the result of formatting will appear, so that the formatter can provide the most appropriate result.

For example, when formatting a date or date symbol for a French locale, you want the month name to be capitalized if it appears at the beginning of the sentence (“Juin est mon mois de naissance”), but not if it appears elsewhere (“Mon mois de naissance est juin”).

If the formatting context isn’t known ahead of time, specify [`Formatter.Context.dynamic`](./context/dynamic.md) to have the system determine the context automatically.

## Topics

### Constants
- [Formatter.Context.unknown](./context/unknown.md)
  An unknown formatting context.
- [Formatter.Context.dynamic](./context/dynamic.md)
  A formatting context determined automatically at runtime.
- [Formatter.Context.standalone](./context/standalone.md)
  The formatting context for stand-alone usage.
- [Formatter.Context.listItem](./context/listitem.md)
  The formatting context for a list or menu item.
- [Formatter.Context.beginningOfSentence](./context/beginningofsentence.md)
  The formatting context for the beginning of a sentence.
- [Formatter.Context.middleOfSentence](./context/middleofsentence.md)
  The formatting context for the middle of a sentence.
### Initializers
- [init?(rawValue: Int)](./context/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [Formatter.UnitStyle](./unitstyle.md)
  Specifies the width of the unit, determining the textual representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter/context)*