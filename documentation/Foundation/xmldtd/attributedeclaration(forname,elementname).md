# attributeDeclaration(forName:elementName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the DTD node representing an attribute-list declaration for a given attribute and its element.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func attributeDeclaration(forName name: String, elementName: String) -> XMLDTDNode?
```

```objc
- (NSXMLDTDNode *) attributeDeclarationForName:(NSString *) name elementName:(NSString *) elementName;
```

## Return Value

An autoreleased [`XMLDTDNode`](../xmldtdnode.md) object, or `nil` if there is no matching attribute-list declaration.

## Discussion

For example, in the attribute-list declaration:

```objc
<!ATTLIST person idnum CDATA "0000">
```

“idnum” would correspond to `attrName` and “person” would correspond to `elementName`.

## Parameters

- `name`: A string object identifying the name of an attribute.
- `elementName`: A string object identifying the name of an element.

## See Also

### Getting DTD Nodes by Name
- [class func predefinedEntityDeclaration(forName: String) -> XMLDTDNode?](./predefinedentitydeclaration%28forname%29.md)
  Returns a DTD node representing the predefined entity declaration with the specified name.
- [func elementDeclaration(forName: String) -> XMLDTDNode?](./elementdeclaration%28forname%29.md)
  Returns the DTD node representing an element declaration for a specified element.
- [func entityDeclaration(forName: String) -> XMLDTDNode?](./entitydeclaration%28forname%29.md)
  Returns the DTD node representing the entity declaration for a specified entity.
- [func notationDeclaration(forName: String) -> XMLDTDNode?](./notationdeclaration%28forname%29.md)
  Returns the DTD node representing the notation declaration identified by the specified notation name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldtd/attributedeclaration(forname:elementname:))*