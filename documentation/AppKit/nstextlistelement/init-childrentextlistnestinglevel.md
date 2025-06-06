# init(children:textList:nestingLevel:)

**Framework**: AppKit  
**Kind**: init

Creates a text list element with the list elements and nesting level you provide.

**Availability**:
- macOS 13.0+

## Declaration

```swift
convenience init?(children: [NSTextListElement], textList: NSTextList, nestingLevel: Int)
```

## Parameters

- `children`: An array of   elements.
- `textList`: The   to add elements to.
- `nestingLevel`: An integer value that describes the level of nesting of these elements.

## See Also

- [convenience init(contents: NSAttributedString, markerAttributes: [NSAttributedString.Key : Any]?, textList: NSTextList, children: [NSTextListElement]?)](nstextlistelement/init(contents:markerattributes:textlist:children:).md)
  Creates a text list element with the list elements, nesting level, and marker attributes you provide.
- [init(parent: NSTextListElement?, textList: NSTextList, contents: NSAttributedString?, markerAttributes: [NSAttributedString.Key : Any]?, children: [NSTextListElement]?)](nstextlistelement/init(parent:textlist:contents:markerattributes:children:).md)
  Creates a text list element with the parent, list elements, nesting level, and marker attributes you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlistelement/init(children:textlist:nestinglevel:))*