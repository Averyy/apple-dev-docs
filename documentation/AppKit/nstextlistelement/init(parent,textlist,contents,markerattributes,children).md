# init(parent:textList:contents:markerAttributes:children:)

**Framework**: AppKit  
**Kind**: init

Creates a text list element with the parent, list elements, nesting level, and marker attributes you provide.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(parent: NSTextListElement?, textList: NSTextList, contents: NSAttributedString?, markerAttributes: [NSAttributedString.Key : Any]? = nil, children: [NSTextListElement]?)
```

## Parameters

- `parent`: The parent `NSTextListElement` of this element, if any.
- `textList`: The [`NSTextList`](nstextlist.md) to add elements to.
- `contents`: An [`NSAttributedString`](https://developer.apple.com/documentation/foundation/nsattributedstring) that contains the contents of the text list element.
- `markerAttributes`: A dictionary of [`NSAttributedString.Key`](https://developer.apple.com/documentation/foundation/nsattributedstring/key) keys and IDs that describe the marker attributes.
- `children`: An array of [`NSTextListElement`](nstextlistelement.md) elements.

## See Also

- [convenience init?(children: [NSTextListElement], textList: NSTextList, nestingLevel: Int)](nstextlistelement/init(children:textlist:nestinglevel:).md)
  Creates a text list element with the list elements and nesting level you provide.
- [convenience init(contents: NSAttributedString, markerAttributes: [NSAttributedString.Key : Any]?, textList: NSTextList, children: [NSTextListElement]?)](nstextlistelement/init(contents:markerattributes:textlist:children:).md)
  Creates a text list element with the list elements, nesting level, and marker attributes you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlistelement/init(parent:textlist:contents:markerattributes:children:))*