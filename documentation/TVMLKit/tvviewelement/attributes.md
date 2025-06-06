# attributes

**Framework**: TVMLKit  
**Kind**: property

The attributes associated with a view element.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var attributes: [String : String]? { get }
```

#### Discussion

All of the attributes are defined as key-value pairs.

## See Also

- [var autoHighlightIdentifier: String?](tvviewelement/autohighlightidentifier.md)
  A string identifying the element that is initially in focus.
- [var children: [TVViewElement]?](tvviewelement/children.md)
  An array containing the child elements of the element currently being inspected.
- [var isDisabled: Bool](tvviewelement/isdisabled.md)
  Boolean value indicating whether the current element being inspected is disabled.
- [var identifier: String](tvviewelement/identifier.md)
  A string containing the unique identifier for an element.
- [var name: String](tvviewelement/name.md)
  A string containing the element’s name.
- [var parent: TVViewElement?](tvviewelement/parent.md)
  The parent of the current node.
- [var style: TVViewElementStyle?](tvviewelement/style.md)
  The style applied to an element.
- [var updateType: TVElementUpdateType](tvviewelement/updatetype.md)
  The value that describes any changes to the DOM tree after it has been reparsed.
- [enum TVElementUpdateType](tvelementupdatetype.md)
  Describes any changes to the DOM tree after it has been reparsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelement/attributes)*