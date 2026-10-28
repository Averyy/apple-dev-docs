# notationDeclaration(forName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the DTD node representing the notation declaration identified by the specified notation name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func notationDeclaration(forName name: String) -> XMLDTDNode?
```

```objc
- (NSXMLDTDNode *) notationDeclarationForName:(NSString *) name;
```

## Return Value

An autoreleased [`XMLDTDNode`](../xmldtdnode.md) object, or `nil` if there is no match.

## Parameters

- `name`: A string that is the name of a notation.

## See Also

### Getting DTD Nodes by Name
- [class func predefinedEntityDeclaration(forName: String) -> XMLDTDNode?](./predefinedentitydeclaration%28forname%29.md)
  Returns a DTD node representing the predefined entity declaration with the specified name.
- [func elementDeclaration(forName: String) -> XMLDTDNode?](./elementdeclaration%28forname%29.md)
  Returns the DTD node representing an element declaration for a specified element.
- [func attributeDeclaration(forName: String, elementName: String) -> XMLDTDNode?](./attributedeclaration%28forname,elementname%29.md)
  Returns the DTD node representing an attribute-list declaration for a given attribute and its element.
- [func entityDeclaration(forName: String) -> XMLDTDNode?](./entitydeclaration%28forname%29.md)
  Returns the DTD node representing the entity declaration for a specified entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/notationdeclaration(forname:))*