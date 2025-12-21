# Formatter.Context.dynamic

**Framework**: Foundation  
**Kind**: case

A formatting context determined automatically at runtime.

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
case dynamic
```

#### Discussion

A [`Formatter.Context.dynamic`](formatter/context/dynamic.md) context is automatically determined to be one of the following: [`Formatter.Context.standalone`](formatter/context/standalone.md), [`Formatter.Context.beginningOfSentence`](formatter/context/beginningofsentence.md), or [`Formatter.Context.middleOfSentence`](formatter/context/middleofsentence.md).

When used in combination with [`stringWithFormat:`](nsstring/stringwithformat:.md), the formatter returns a string proxy, formats the string using [`Formatter.Context.unknown`](formatter/context/unknown.md), determines context based on the proxy string’s location, and then reformats the string accordingly.

## See Also

- [Formatter.Context.unknown](formatter/context/unknown.md)
  An unknown formatting context.
- [Formatter.Context.standalone](formatter/context/standalone.md)
  The formatting context for stand-alone usage.
- [Formatter.Context.listItem](formatter/context/listitem.md)
  The formatting context for a list or menu item.
- [Formatter.Context.beginningOfSentence](formatter/context/beginningofsentence.md)
  The formatting context for the beginning of a sentence.
- [Formatter.Context.middleOfSentence](formatter/context/middleofsentence.md)
  The formatting context for the middle of a sentence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatter/context/dynamic)*