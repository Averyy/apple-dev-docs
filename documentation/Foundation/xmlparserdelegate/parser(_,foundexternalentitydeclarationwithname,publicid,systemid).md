# parser(_:foundExternalEntityDeclarationWithName:publicID:systemID:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent by a parser object to its delegate when it encounters an external entity declaration.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func parser(_ parser: XMLParser, foundExternalEntityDeclarationWithName name: String, publicID: String?, systemID: String?)
```

```objc
- (void) parser:(NSXMLParser *) parser foundExternalEntityDeclarationWithName:(NSString *) name publicID:(NSString *) publicID systemID:(NSString *) systemID;
```

## Parameters

- `parser`: An `NSXMLParser` object parsing XML.
- `name`: A string that is the name of an entity.
- `publicID`: A string that specifies the public ID associated with `entityName`.
- `systemID`: A string that specifies the system ID associated with `entityName`.

## See Also

### Related Documentation
- [func parser(XMLParser, resolveExternalEntityName: String, systemID: String?) -> Data?](./parser%28_,resolveexternalentityname,systemid%29.md)
  Sent by a parser object to its delegate when it encounters a given external entity with a specific system ID.
### Handling the DTD
- [func parser(XMLParser, foundAttributeDeclarationWithName: String, forElement: String, type: String?, defaultValue: String?)](./parser%28_,foundattributedeclarationwithname,forelement,type,defaultvalue%29.md)
  Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.
- [func parser(XMLParser, foundElementDeclarationWithName: String, model: String)](./parser%28_,foundelementdeclarationwithname,model%29.md)
  Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.
- [func parser(XMLParser, foundInternalEntityDeclarationWithName: String, value: String?)](./parser%28_,foundinternalentitydeclarationwithname,value%29.md)
  Sent by a parser object to the delegate when it encounters an internal entity declaration.
- [func parser(XMLParser, foundUnparsedEntityDeclarationWithName: String, publicID: String?, systemID: String?, notationName: String?)](./parser%28_,foundunparsedentitydeclarationwithname,publicid,systemid,notationname%29.md)
  Sent by a parser object to its delegate when it encounters an unparsed entity declaration.
- [func parser(XMLParser, foundNotationDeclarationWithName: String, publicID: String?, systemID: String?)](./parser%28_,foundnotationdeclarationwithname,publicid,systemid%29.md)
  Sent by a parser object to its delegate when it encounters a notation declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:foundexternalentitydeclarationwithname:publicid:systemid:))*