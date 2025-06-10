# xmlString

**Framework**: Foundation  
**Kind**: property

Returns the string representation of the receiver as it would appear in an XML document.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var xmlString: String { get }
```

#### Discussion

The returned string includes the string representations of all children. This method invokes [`xmlString(options:)`](xmlnode/xmlstring(options:).md) with an `options` argument of `NSXMLNodeOptionsNone`.

## See Also

- [func xmlString(options: XMLNode.Options) -> String](xmlnode/xmlstring(options:).md)
  Returns the string representation of the receiver as it would appear in an XML document, with one or more output options specified.
- [func canonicalXMLStringPreservingComments(Bool) -> String](xmlnode/canonicalxmlstringpreservingcomments(_:).md)
  Returns a string object encapsulating the receiver’s XML in canonical form.
- [var description: String](xmlnode/description.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/xmlstring)*