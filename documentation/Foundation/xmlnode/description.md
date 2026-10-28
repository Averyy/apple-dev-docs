# description

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var description: String { get }
```

```objc
@property (copy, readonly) NSString * description;
```

## Discussion

Used for debugging. May give more information than XMLString.

## See Also

### Emitting Node Content
- [var xmlString: String](./xmlstring.md)
  Returns the string representation of the receiver as it would appear in an XML document.
- [func xmlString(options: XMLNode.Options) -> String](./xmlstring%28options%29.md)
  Returns the string representation of the receiver as it would appear in an XML document, with one or more output options specified.
- [func canonicalXMLStringPreservingComments(Bool) -> String](./canonicalxmlstringpreservingcomments%28_%29.md)
  Returns a string object encapsulating the receiver’s XML in canonical form.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/description)*