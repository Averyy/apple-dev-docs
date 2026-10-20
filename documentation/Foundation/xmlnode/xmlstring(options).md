# xmlString(options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the string representation of the receiver as it would appear in an XML document, with one or more output options specified.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func xmlString(options: XMLNode.Options = []) -> String
```

```objc
- (NSString *) XMLStringWithOptions:(NSXMLNodeOptions) options;
```

#### Discussion

The returned string includes the string representations of all children.

## Parameters

- `options`: One or more `enum` constants identifying an output option; bit-OR multiple constants together.  See Constants for a list of valid constants for specifying output options.

## See Also

### Emitting Node Content
- [var xmlString: String](./xmlstring.md)
  Returns the string representation of the receiver as it would appear in an XML document.
- [func canonicalXMLStringPreservingComments(Bool) -> String](./canonicalxmlstringpreservingcomments%28_%29.md)
  Returns a string object encapsulating the receiver’s XML in canonical form.
- [var description: String](./description.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/xmlstring(options:))*