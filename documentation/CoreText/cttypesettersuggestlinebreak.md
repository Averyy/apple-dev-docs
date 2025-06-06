# CTTypesetterSuggestLineBreak(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Suggests a contextual line breakpoint based on the width provided.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTTypesetterSuggestLineBreak(_ typesetter: CTTypesetter, _ startIndex: CFIndex, _ width: Double) -> CFIndex
```

#### Return Value

A count of the characters from `startIndex` that would cause the line break. The value returned can be used to construct a character range for [`CTTypesetterCreateLine(_:_:)`](cttypesettercreateline(_:_:).md).

#### Discussion

The line break can be triggered either by a hard-break character in the stream or by filling the specified width with characters. This function is equivalent to [`CTTypesetterSuggestLineBreakWithOffset(_:_:_:_:)`](cttypesettersuggestlinebreakwithoffset(_:_:_:_:).md) with an offset of 0.0.

## Parameters

- `typesetter`: The typesetter that creates the line. This parameter is required and cannot be set to  .
- `startIndex`: The starting point for the line-break calculations. The break calculations include the character starting at  .
- `width`: The requested line-break width.

## See Also

- [func CTTypesetterSuggestLineBreakWithOffset(CTTypesetter, CFIndex, Double, Double) -> CFIndex](cttypesettersuggestlinebreakwithoffset(_:_:_:_:).md)
  Suggests a contextual line breakpoint based on the width provided and the specified offset.
- [func CTTypesetterSuggestClusterBreak(CTTypesetter, CFIndex, Double) -> CFIndex](cttypesettersuggestclusterbreak(_:_:_:).md)
  Suggests a cluster line breakpoint based on the width provided.
- [func CTTypesetterSuggestClusterBreakWithOffset(CTTypesetter, CFIndex, Double, Double) -> CFIndex](cttypesettersuggestclusterbreakwithoffset(_:_:_:_:).md)
  Suggests a cluster line breakpoint based on the specified width and line offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttypesettersuggestlinebreak(_:_:_:))*