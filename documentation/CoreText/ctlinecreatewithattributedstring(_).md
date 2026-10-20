# CTLineCreateWithAttributedString(_:)

**Framework**: Core Text  
**Kind**: func  
**Role**: Function

Creates a single immutable line object from an attributed string.

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
func CTLineCreateWithAttributedString(_ attrString: CFAttributedString) -> CTLine
```

```c
extern CTLineRefCTLineCreateWithAttributedString(CFAttributedStringRef attrString);
```

#### Return Value

A reference to a [`CTLine`](./ctline.md) object.

#### Discussion

This function allows clients to create a line without creating a [`CTTypesetter`](./cttypesetter.md) object. The framework provides a typesetter for single-line typesetting under the hood. Simple elements that don’t require line breaks, such as text labels, can use this API.

## Parameters

- `attrString`: The string that creates the line.

## See Also

### Related Documentation
- [func CTTypesetterCreateWithAttributedString(CFAttributedString) -> CTTypesetter](./cttypesettercreatewithattributedstring%28_%29.md)
  Creates an immutable typesetter object using an attributed string.
- [func CTTypesetterCreateWithAttributedStringAndOptions(CFAttributedString, CFDictionary?) -> CTTypesetter?](./cttypesettercreatewithattributedstringandoptions%28_,_%29.md)
  Creates an immutable typesetter object using an attributed string and a dictionary of options.
- [func CTTypesetterCreateLine(CTTypesetter, CFRange) -> CTLine](./cttypesettercreateline%28_,_%29.md)
  Creates an immutable line from the typesetter.
### Creating Lines
- [func CTLineCreateTruncatedLine(CTLine, Double, CTLineTruncationType, CTLine?) -> CTLine?](./ctlinecreatetruncatedline%28_,_,_,_%29.md)
  Creates a truncated line from an existing line.
- [func CTLineCreateJustifiedLine(CTLine, CGFloat, Double) -> CTLine?](./ctlinecreatejustifiedline%28_,_,_%29.md)
  Creates a justified line from an existing line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlinecreatewithattributedstring(_:))*