# CTTypesetterCreateLineWithOffset(_:_:_:)

**Framework**: Core Text  
**Kind**: func

Creates an immutable line from the typesetter at a specified line offset.

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
func CTTypesetterCreateLineWithOffset(_ typesetter: CTTypesetter, _ stringRange: CFRange, _ offset: Double) -> CTLine
```

#### Return Value

A reference to a CTLine object if the call was successful; otherwise, `NULL`.

#### Discussion

The resultant line consists of glyphs in the correct visual order, ready to draw.

## Parameters

- `typesetter`: The typesetter that creates the line. This parameter is required and cannot be set to  .
- `stringRange`: The string range on which the line is based. If the length portion of range is set to  , then the typesetter continues to add glyphs to the line until it runs out of characters in the string. The location and length of the range must be within the bounds of the string, or the call will fail.
- `offset`: The line position offset.

## See Also

- [func CTTypesetterCreateLine(CTTypesetter, CFRange) -> CTLine](cttypesettercreateline(_:_:).md)
  Creates an immutable line from the typesetter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttypesettercreatelinewithoffset(_:_:_:))*