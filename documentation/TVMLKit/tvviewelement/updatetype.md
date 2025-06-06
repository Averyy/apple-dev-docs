# updateType

**Framework**: TVMLKit  
**Kind**: property

The value that describes any changes to the DOM tree after it has been reparsed.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
var updateType: TVElementUpdateType { get }
```

#### Discussion

For possible values, see [`TVElementUpdateType`](tvelementupdatetype.md). This property is initially set to [`TVElementUpdateType.none`](tvelementupdatetype/none.md).

## See Also

- [var autoHighlightIdentifier: String?](tvviewelement/autohighlightidentifier.md)
  A string identifying the element that is initially in focus.
- [var attributes: [String : String]?](tvviewelement/attributes.md)
  The attributes associated with a view element.
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
- [enum TVElementUpdateType](tvelementupdatetype.md)
  Describes any changes to the DOM tree after it has been reparsed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelement/updatetype)*