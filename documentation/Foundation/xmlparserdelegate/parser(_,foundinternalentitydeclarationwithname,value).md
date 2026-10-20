# parser(_:foundInternalEntityDeclarationWithName:value:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sent by a parser object to the delegate when it encounters an internal entity declaration.

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
optional func parser(_ parser: XMLParser, foundInternalEntityDeclarationWithName name: String, value: String?)
```

```objc
- (void) parser:(NSXMLParser *) parser foundInternalEntityDeclarationWithName:(NSString *) name value:(NSString *) value;
```

## Parameters

- `parser`: An `NSXMLParser` object parsing XML.
- `name`: A string that is the declared name of an internal entity.
- `value`: A string that is the value of entity `name`.

## See Also

### Handling the DTD
- [func parser(XMLParser, foundAttributeDeclarationWithName: String, forElement: String, type: String?, defaultValue: String?)](./parser%28_,foundattributedeclarationwithname,forelement,type,defaultvalue%29.md)
  Sent by a parser object to its delegate when it encounters a declaration of an attribute that is associated with a specific element.
- [func parser(XMLParser, foundElementDeclarationWithName: String, model: String)](./parser%28_,foundelementdeclarationwithname,model%29.md)
  Sent by a parser object to its delegate when it encounters a declaration of an element with a given model.
- [func parser(XMLParser, foundExternalEntityDeclarationWithName: String, publicID: String?, systemID: String?)](./parser%28_,foundexternalentitydeclarationwithname,publicid,systemid%29.md)
  Sent by a parser object to its delegate when it encounters an external entity declaration.
- [func parser(XMLParser, foundUnparsedEntityDeclarationWithName: String, publicID: String?, systemID: String?, notationName: String?)](./parser%28_,foundunparsedentitydeclarationwithname,publicid,systemid,notationname%29.md)
  Sent by a parser object to its delegate when it encounters an unparsed entity declaration.
- [func parser(XMLParser, foundNotationDeclarationWithName: String, publicID: String?, systemID: String?)](./parser%28_,foundnotationdeclarationwithname,publicid,systemid%29.md)
  Sent by a parser object to its delegate when it encounters a notation declaration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparserdelegate/parser(_:foundinternalentitydeclarationwithname:value:))*