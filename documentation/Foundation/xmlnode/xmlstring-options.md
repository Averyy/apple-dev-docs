# xmlString(options:)

**Framework**: Foundation  
**Kind**: method

Returns the string representation of the receiver as it would appear in an XML document, with one or more output options specified.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func xmlString(options: XMLNode.Options = []) -> String
```

#### Discussion

The returned string includes the string representations of all children.

## Parameters

- `options`: One or more   constants identifying an output option; bit-OR multiple constants together.  See Constants for a list of valid constants for specifying output options.

## See Also

- [var xmlString: String](xmlnode/xmlstring.md)
  Returns the string representation of the receiver as it would appear in an XML document.
- [func canonicalXMLStringPreservingComments(Bool) -> String](xmlnode/canonicalxmlstringpreservingcomments(_:).md)
  Returns a string object encapsulating the receiver’s XML in canonical form.
- [var description: String](xmlnode/description.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/xmlstring(options:))*