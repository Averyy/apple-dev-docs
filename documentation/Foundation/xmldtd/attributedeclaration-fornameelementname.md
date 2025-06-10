# attributeDeclaration(forName:elementName:)

**Framework**: Foundation  
**Kind**: method

Returns the DTD node representing an attribute-list declaration for a given attribute and its element.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func attributeDeclaration(forName name: String, elementName: String) -> XMLDTDNode?
```

#### Return Value

An autoreleased [`XMLDTDNode`](xmldtdnode.md) object, or `nil` if there is no matching attribute-list declaration.

#### Discussion

For example, in the attribute-list declaration:

```objc
<!ATTLIST person idnum CDATA "0000">
```

“idnum” would correspond to `attrName` and “person” would correspond to `elementName`.

## Parameters

- `name`: A string object identifying the name of an attribute.
- `elementName`: A string object identifying the name of an element.

## See Also

- [class func predefinedEntityDeclaration(forName: String) -> XMLDTDNode?](xmldtd/predefinedentitydeclaration(forname:).md)
  Returns a DTD node representing the predefined entity declaration with the specified name.
- [func elementDeclaration(forName: String) -> XMLDTDNode?](xmldtd/elementdeclaration(forname:).md)
  Returns the DTD node representing an element declaration for a specified element.
- [func entityDeclaration(forName: String) -> XMLDTDNode?](xmldtd/entitydeclaration(forname:).md)
  Returns the DTD node representing the entity declaration for a specified entity.
- [func notationDeclaration(forName: String) -> XMLDTDNode?](xmldtd/notationdeclaration(forname:).md)
  Returns the DTD node representing the notation declaration identified by the specified notation name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/attributedeclaration(forname:elementname:))*