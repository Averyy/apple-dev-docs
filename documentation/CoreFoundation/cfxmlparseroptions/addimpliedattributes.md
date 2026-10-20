# addImpliedAttributes

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.

**Availability**:
- macOS

## Declaration

```swift
static var addImpliedAttributes: CFXMLParserOptions { get }
```

```c
kCFXMLParserAddImpliedAttributes
```

## See Also

### Constants
- [static var validateDocument: CFXMLParserOptions](./validatedocument.md)
  Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [static var skipMetaData: CFXMLParserOptions](./skipmetadata.md)
  Silently skip over metadata constructs (the DTD and comments).
- [static var replacePhysicalEntities: CFXMLParserOptions](./replacephysicalentities.md)
  Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.
- [static var skipWhitespace: CFXMLParserOptions](./skipwhitespace.md)
- [static var resolveExternalEntities: CFXMLParserOptions](./resolveexternalentities.md)
  Resolves all external entities.
- [static var allOptions: CFXMLParserOptions](./alloptions.md)
  Makes the parser do the most work, returning only the pure elementtree.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions/addimpliedattributes)*