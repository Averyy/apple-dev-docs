# init(children:textList:nestingLevel:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a text list element with the list elements and nesting level you provide.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(children: [NSTextListElement], textList: NSTextList, nestingLevel: Int)
```

```objc
+ (instancetype) textListElementWithChildElements:(NSArray<NSTextListElement *> *) children textList:(NSTextList *) textList nestingLevel:(NSInteger) nestingLevel;
```

## Parameters

- `children`: An array of [`NSTextListElement`](../nstextlistelement.md) elements.
- `textList`: The [`NSTextList`](../nstextlist.md) to add elements to.
- `nestingLevel`: An integer value that describes the level of nesting of these elements.

## See Also

### Create a text list element
- [convenience init(contents: NSAttributedString, markerAttributes: [NSAttributedString.Key : Any]?, textList: NSTextList, children: [NSTextListElement]?)](./init%28contents,markerattributes,textlist,children%29.md)
  Creates a text list element with the list elements, nesting level, and marker attributes you provide.
- [init(parent: NSTextListElement?, textList: NSTextList, contents: NSAttributedString?, markerAttributes: [NSAttributedString.Key : Any]?, children: [NSTextListElement]?)](./init%28parent,textlist,contents,markerattributes,children%29.md)
  Creates a text list element with the parent, list elements, nesting level, and marker attributes you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlistelement/init(children:textlist:nestinglevel:))*