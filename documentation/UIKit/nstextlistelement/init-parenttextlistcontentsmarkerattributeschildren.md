# init(parent:textList:contents:markerAttributes:children:)

**Framework**: UIKit  
**Kind**: init

Creates a text list element with the parent, list elements, nesting level, and marker attributes you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(parent: NSTextListElement?, textList: NSTextList, contents: NSAttributedString?, markerAttributes: [NSAttributedString.Key : Any]? = nil, children: [NSTextListElement]?)
```

## Parameters

- `parent`: The parent   of this element, if any.
- `textList`: The   to add elements to.
- `contents`: An   that contains the contents of the text list element.
- `markerAttributes`: A dictionary of   keys and IDs that describe the marker attributes.
- `children`: An array of   elements.

## See Also

- [convenience init?(children: [NSTextListElement], textList: NSTextList, nestingLevel: Int)](nstextlistelement/init(children:textlist:nestinglevel:).md)
  Creates a text list element with the list elements and nesting level you provide.
- [convenience init(contents: NSAttributedString, markerAttributes: [NSAttributedString.Key : Any]?, textList: NSTextList, children: [NSTextListElement]?)](nstextlistelement/init(contents:markerattributes:textlist:children:).md)
  Creates a text list element with the list elements, nesting level, and marker attributes you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlistelement/init(parent:textlist:contents:markerattributes:children:))*