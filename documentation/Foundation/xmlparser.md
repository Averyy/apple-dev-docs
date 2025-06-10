# XMLParser

**Framework**: Foundation  
**Kind**: class

An event driven parser of XML documents (including DTD declarations).

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
class XMLParser
```

#### Overview

An [`XMLParser`](xmlparser.md) notifies its delegate about the items (elements, attributes, CDATA blocks, comments, and so on) that it encounters as it processes an XML document. It does not itself do anything with those parsed items except report them. It also reports parsing errors. For convenience, an [`XMLParser`](xmlparser.md) object in the following descriptions is sometimes referred to as a parser object. Unless used in a callback, the [`XMLParser`](xmlparser.md) is a thread-safe class as long as any given instance is only used in one thread.

> **Note**:  Namespace support was implemented in [`XMLParser`](xmlparser.md) starting in macOS 10.4. Namespace-related methods of [`XMLParser`](xmlparser.md) prior to this version have no effect.

## Topics

### Initializing a Parser Object
- [convenience init?(contentsOf: URL)](xmlparser/init(contentsof:).md)
  Initializes a parser with the XML content referenced by the given URL.
- [init(data: Data)](xmlparser/init(data:).md)
  Initializes a parser with the XML contents encapsulated in a given data object.
- [convenience init(stream: InputStream)](xmlparser/init(stream:).md)
  Initializes a parser with the XML contents from the specified stream and parses it.
### Managing Delegates
- [var delegate: (any XMLParserDelegate)?](xmlparser/delegate.md)
  A delegate object that receives messages about the parsing process.
### Managing Parser Behavior
- [var shouldProcessNamespaces: Bool](xmlparser/shouldprocessnamespaces.md)
  A Boolean value that determines whether the parser reports the namespaces and qualified names of elements.
- [var shouldReportNamespacePrefixes: Bool](xmlparser/shouldreportnamespaceprefixes.md)
  A Boolean value that determines whether the parser reports the prefixes indicating the scope of namespace declarations.
- [var shouldResolveExternalEntities: Bool](xmlparser/shouldresolveexternalentities.md)
  A Boolean value that determines whether the parser reports declarations of external entities.
### Parsing
- [func parse() -> Bool](xmlparser/parse.md)
  Starts the event-driven parsing operation.
- [func abortParsing()](xmlparser/abortparsing.md)
  Stops the parser object.
- [var parserError: (any Error)?](xmlparser/parsererror.md)
  An [`NSError`](nserror.md) object from which you can obtain information about a parsing error.
### Obtaining Parser State
- [var columnNumber: Int](xmlparser/columnnumber.md)
  The column number of the XML document being processed by the parser.
- [var lineNumber: Int](xmlparser/linenumber.md)
  The line number of the XML document being processed by the parser.
- [var publicID: String?](xmlparser/publicid.md)
  The public identifier of the external entity referenced in the XML document.
- [var systemID: String?](xmlparser/systemid.md)
  The system identifier of the external entity referenced in the XML document.
### Constants
- [XMLParser.ExternalEntityResolvingPolicy](xmlparser/externalentityresolvingpolicy-swift.enum.md)
- [class let errorDomain: String](xmlparser/errordomain.md)
  Indicates an error in XML parsing.
- [XMLParser.ErrorCode](xmlparser/errorcode.md)
  The following error codes are defined by `NSXMLParser`. For error codes not listed here, see the `<libxml/xmlerror.h>` header file.
### Instance Properties
- [var allowedExternalEntityURLs: Set<URL>?](xmlparser/allowedexternalentityurls.md)
- [var externalEntityResolvingPolicy: XMLParser.ExternalEntityResolvingPolicy](xmlparser/externalentityresolvingpolicy-swift.property.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol XMLParserDelegate](xmlparserdelegate.md)
  The interface an XML parser uses to inform its delegate about the content of the parsed document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlparser)*