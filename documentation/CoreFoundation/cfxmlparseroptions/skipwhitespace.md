# skipWhitespace

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

**Availability**:
- macOS

## Declaration

```swift
static var skipWhitespace: CFXMLParserOptions { get }
```

```c
kCFXMLParserSkipWhitespace
```

#### Discussion

Skip over all whitespace that does not abut non-whitespace character data. In other words, given “`<foo>  <bar> blah </bar></foo>`,” the whitespace between foo’s open tag and bar’s open tag would be suppressed, but the whitespace around `blah` would be preserved.

## See Also

### Constants
- [static var validateDocument: CFXMLParserOptions](./validatedocument.md)
  Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [static var skipMetaData: CFXMLParserOptions](./skipmetadata.md)
  Silently skip over metadata constructs (the DTD and comments).
- [static var replacePhysicalEntities: CFXMLParserOptions](./replacephysicalentities.md)
  Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.
- [static var resolveExternalEntities: CFXMLParserOptions](./resolveexternalentities.md)
  Resolves all external entities.
- [static var addImpliedAttributes: CFXMLParserOptions](./addimpliedattributes.md)
  Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.
- [static var allOptions: CFXMLParserOptions](./alloptions.md)
  Makes the parser do the most work, returning only the pure elementtree.
- [kCFXMLParserNoOptions](./kcfxmlparsernooptions.md)
  Leaves the XML as “intact” as possible (reports all structures; performs no replacements).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions/skipwhitespace)*