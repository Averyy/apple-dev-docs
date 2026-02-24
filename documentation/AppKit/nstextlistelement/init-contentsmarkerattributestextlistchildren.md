# init(contents:markerAttributes:textList:children:)

**Framework**: AppKit  
**Kind**: init

Creates a text list element with the list elements, nesting level, and marker attributes you provide.

**Availability**:
- macOS 13.0+

## Declaration

```swift
convenience init(contents: NSAttributedString, markerAttributes: [NSAttributedString.Key : Any]? = nil, textList: NSTextList, children: [NSTextListElement]?)
```

## Parameters

- `contents`: An [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) that contains the contents of the text list element.
- `markerAttributes`: A dictionary of [`NSAttributedString.Key`](https://developer.apple.com/documentation/Foundation/NSAttributedString/Key) keys and IDs that describe the marker attributes.
- `textList`: The [`NSTextList`](nstextlist.md) to add elements to.
- `children`: An array of [`NSTextListElement`](nstextlistelement.md) elements.

## See Also

- [convenience init?(children: [NSTextListElement], textList: NSTextList, nestingLevel: Int)](nstextlistelement/init(children:textlist:nestinglevel:).md)
  Creates a text list element with the list elements and nesting level you provide.
- [init(parent: NSTextListElement?, textList: NSTextList, contents: NSAttributedString?, markerAttributes: [NSAttributedString.Key : Any]?, children: [NSTextListElement]?)](nstextlistelement/init(parent:textlist:contents:markerattributes:children:).md)
  Creates a text list element with the parent, list elements, nesting level, and marker attributes you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlistelement/init(contents:markerattributes:textlist:children:))*