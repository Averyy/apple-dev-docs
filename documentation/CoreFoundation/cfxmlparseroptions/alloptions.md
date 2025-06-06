# allOptions

**Framework**: Core Foundation  
**Kind**: property

Makes the parser do the most work, returning only the pure elementtree.

**Availability**:
- macOS ?+

## Declaration

```swift
static var allOptions: CFXMLParserOptions { get }
```

## See Also

- [static var validateDocument: CFXMLParserOptions](cfxmlparseroptions/validatedocument.md)
  Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [static var skipMetaData: CFXMLParserOptions](cfxmlparseroptions/skipmetadata.md)
  Silently skip over metadata constructs (the DTD and comments).
- [static var replacePhysicalEntities: CFXMLParserOptions](cfxmlparseroptions/replacephysicalentities.md)
  Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.
- [static var skipWhitespace: CFXMLParserOptions](cfxmlparseroptions/skipwhitespace.md)
- [static var resolveExternalEntities: CFXMLParserOptions](cfxmlparseroptions/resolveexternalentities.md)
  Resolves all external entities.
- [static var addImpliedAttributes: CFXMLParserOptions](cfxmlparseroptions/addimpliedattributes.md)
  Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions/alloptions)*