# CFXMLParserOptions

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

Options you can use to control the parser’s treatment of an XML document.

**Availability**:
- macOS

## Declaration

```swift
struct CFXMLParserOptions
```

```c
enum CFXMLParserOptions : CFOptionFlags;
```

#### Overview

These are the various options you use to configure the parser. An option flag of 0 ([`kCFXMLParserNoOptions`](./cfxmlparseroptions/kcfxmlparsernooptions.md)) leaves the XML as “intact” as possible (reports all structures; performs no replacements). Hence, to make the parser do the most work, returning only the pure element tree, set the option flag to [`allOptions`](./cfxmlparseroptions/alloptions.md).

## Topics

### Constants
- [static var validateDocument: CFXMLParserOptions](./cfxmlparseroptions/validatedocument.md)
  Validates the document against its grammar from the DTD, reporting any errors. Currently not supported.
- [static var skipMetaData: CFXMLParserOptions](./cfxmlparseroptions/skipmetadata.md)
  Silently skip over metadata constructs (the DTD and comments).
- [static var replacePhysicalEntities: CFXMLParserOptions](./cfxmlparseroptions/replacephysicalentities.md)
  Replaces declared entities like `&lt`;. Note that other than the 5 predefined entities (`lt`, `gt`, `quot`, `amp`, `apos`), these must be defined in the DTD. Currently not supported.
- [static var skipWhitespace: CFXMLParserOptions](./cfxmlparseroptions/skipwhitespace.md)
- [static var resolveExternalEntities: CFXMLParserOptions](./cfxmlparseroptions/resolveexternalentities.md)
  Resolves all external entities.
- [static var addImpliedAttributes: CFXMLParserOptions](./cfxmlparseroptions/addimpliedattributes.md)
  Where the DTD specifies implied attribute-value pairs for a particular element, add those pairs to any occurrences of the element in the element tree. Currently not supported.
- [static var allOptions: CFXMLParserOptions](./cfxmlparseroptions/alloptions.md)
  Makes the parser do the most work, returning only the pure elementtree.
- [kCFXMLParserNoOptions](./cfxmlparseroptions/kcfxmlparsernooptions.md)
  Leaves the XML as “intact” as possible (reports all structures; performs no replacements).
### Initializers
- [init(rawValue: CFOptionFlags)](./cfxmlparseroptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [struct CFXMLParserStatusCode](./cfxmlparserstatuscode.md)
  The various status and error flags that can be returned by the parser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfxmlparseroptions)*