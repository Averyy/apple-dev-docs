# init(parent:textList:contents:markerAttributes:children:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a text list element with the parent, list elements, nesting level, and marker attributes you provide.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(parent: NSTextListElement?, textList: NSTextList, contents: NSAttributedString?, markerAttributes: [NSAttributedString.Key : Any]? = nil, children: [NSTextListElement]?)
```

```objc
- (instancetype) initWithParentElement:(NSTextListElement *) parent textList:(NSTextList *) textList contents:(NSAttributedString *) contents markerAttributes:(NSDictionary<NSString *,id> *) markerAttributes childElements:(NSArray<NSTextListElement *> *) children;
```

## Parameters

- `parent`: The parent `NSTextListElement` of this element, if any.
- `textList`: The [`NSTextList`](../nstextlist.md) to add elements to.
- `contents`: An [`NSAttributedString`](../../Foundation/nsattributedstring.md) that contains the contents of the text list element.
- `markerAttributes`: A dictionary of [`NSAttributedString.Key`](../../Foundation/nsattributedstring/key.md) keys and IDs that describe the marker attributes.
- `children`: An array of [`NSTextListElement`](../nstextlistelement.md) elements.

## See Also

### Create a text list element
- [convenience init?(children: [NSTextListElement], textList: NSTextList, nestingLevel: Int)](./init%28children,textlist,nestinglevel%29.md)
  Creates a text list element with the list elements and nesting level you provide.
- [convenience init(contents: NSAttributedString, markerAttributes: [NSAttributedString.Key : Any]?, textList: NSTextList, children: [NSTextListElement]?)](./init%28contents,markerattributes,textlist,children%29.md)
  Creates a text list element with the list elements, nesting level, and marker attributes you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlistelement/init(parent:textlist:contents:markerattributes:children:))*