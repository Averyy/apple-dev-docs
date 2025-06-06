# CTTypesetterCreateLine(_:_:)

**Framework**: Core Text  
**Kind**: func

Creates an immutable line from the typesetter.

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
func CTTypesetterCreateLine(_ typesetter: CTTypesetter, _ stringRange: CFRange) -> CTLine
```

#### Return Value

A reference to a CTLine object if the call was successful; otherwise, `NULL`.

#### Discussion

The resultant line consists of glyphs in the correct visual order, ready to draw. This function is equivalent to [`CTTypesetterCreateLineWithOffset(_:_:_:)`](cttypesettercreatelinewithoffset(_:_:_:).md) with an offset of 0.0.

## Parameters

- `typesetter`: The typesetter that creates the line. This parameter is required and cannot be set to  .
- `stringRange`: The string range on which the line is based. If the length portion of range is set to  , then the typesetter continues to add glyphs to the line until it runs out of characters in the string. The location and length of the range must be within the bounds of the string, or the call will fail.

## See Also

- [func CTTypesetterCreateLineWithOffset(CTTypesetter, CFRange, Double) -> CTLine](cttypesettercreatelinewithoffset(_:_:_:).md)
  Creates an immutable line from the typesetter at a specified line offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttypesettercreateline(_:_:))*