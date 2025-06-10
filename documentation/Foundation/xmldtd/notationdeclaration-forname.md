# notationDeclaration(forName:)

**Framework**: Foundation  
**Kind**: method

Returns the DTD node representing the notation declaration identified by the specified notation name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func notationDeclaration(forName name: String) -> XMLDTDNode?
```

#### Return Value

An autoreleased [`XMLDTDNode`](xmldtdnode.md) object, or `nil` if there is no match.

## Parameters

- `name`: A string that is the name of a notation.

## See Also

- [class func predefinedEntityDeclaration(forName: String) -> XMLDTDNode?](xmldtd/predefinedentitydeclaration(forname:).md)
  Returns a DTD node representing the predefined entity declaration with the specified name.
- [func elementDeclaration(forName: String) -> XMLDTDNode?](xmldtd/elementdeclaration(forname:).md)
  Returns the DTD node representing an element declaration for a specified element.
- [func attributeDeclaration(forName: String, elementName: String) -> XMLDTDNode?](xmldtd/attributedeclaration(forname:elementname:).md)
  Returns the DTD node representing an attribute-list declaration for a given attribute and its element.
- [func entityDeclaration(forName: String) -> XMLDTDNode?](xmldtd/entitydeclaration(forname:).md)
  Returns the DTD node representing the entity declaration for a specified entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/notationdeclaration(forname:))*