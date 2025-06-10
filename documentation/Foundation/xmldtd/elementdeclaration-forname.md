# elementDeclaration(forName:)

**Framework**: Foundation  
**Kind**: method

Returns the DTD node representing an element declaration for a specified element.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func elementDeclaration(forName name: String) -> XMLDTDNode?
```

#### Return Value

An autoreleased [`XMLDTDNode`](xmldtdnode.md) object, or `nil` if there is no match.

## Parameters

- `name`: A string that is the name of an element.

## See Also

- [class func predefinedEntityDeclaration(forName: String) -> XMLDTDNode?](xmldtd/predefinedentitydeclaration(forname:).md)
  Returns a DTD node representing the predefined entity declaration with the specified name.
- [func attributeDeclaration(forName: String, elementName: String) -> XMLDTDNode?](xmldtd/attributedeclaration(forname:elementname:).md)
  Returns the DTD node representing an attribute-list declaration for a given attribute and its element.
- [func entityDeclaration(forName: String) -> XMLDTDNode?](xmldtd/entitydeclaration(forname:).md)
  Returns the DTD node representing the entity declaration for a specified entity.
- [func notationDeclaration(forName: String) -> XMLDTDNode?](xmldtd/notationdeclaration(forname:).md)
  Returns the DTD node representing the notation declaration identified by the specified notation name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/elementdeclaration(forname:))*