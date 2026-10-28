# CTTypesetterSuggestClusterBreakWithOffset(_:_:_:_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Suggests a cluster line breakpoint based on the specified width and line offset.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CTTypesetterSuggestClusterBreakWithOffset(_ typesetter: CTTypesetter, _ startIndex: CFIndex, _ width: Double, _ offset: Double) -> CFIndex
```

```c
extern CFIndex CTTypesetterSuggestClusterBreakWithOffset(CTTypesetterRef typesetter, CFIndex startIndex, double width, double offset);
```

## Return Value

A count of the characters from `startIndex` that would cause the cluster break. The value returned can be used to construct a character range for [`CTTypesetterCreateLine(_:_:)`](./cttypesettercreateline%28_,_%29.md).

## Discussion

This cluster break is similar to a character break, except that it does not break apart linguistic clusters. No other contextual analysis is done. This can be used by the caller to implement a different line-breaking scheme, such as hyphenation. A typographic cluster break can also be triggered by a hard-break character in the stream.

## Parameters

- `typesetter`: The typesetter that creates the line. This parameter is required and cannot be set to `NULL`.
- `startIndex`: The starting point for the typographic cluster-break calculations. The break calculations include the character starting at `startIndex`.
- `width`: The requested typographic cluster-break width.
- `offset`: The line offset position.

## See Also

### Breaking Lines
- [func CTTypesetterSuggestLineBreak(CTTypesetter, CFIndex, Double) -> CFIndex](./cttypesettersuggestlinebreak%28_,_,_%29.md)
  Suggests a contextual line breakpoint based on the width provided.
- [func CTTypesetterSuggestLineBreakWithOffset(CTTypesetter, CFIndex, Double, Double) -> CFIndex](./cttypesettersuggestlinebreakwithoffset%28_,_,_,_%29.md)
  Suggests a contextual line breakpoint based on the width provided and the specified offset.
- [func CTTypesetterSuggestClusterBreak(CTTypesetter, CFIndex, Double) -> CFIndex](./cttypesettersuggestclusterbreak%28_,_,_%29.md)
  Suggests a cluster line breakpoint based on the width provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttypesettersuggestclusterbreakwithoffset(_:_:_:_:))*