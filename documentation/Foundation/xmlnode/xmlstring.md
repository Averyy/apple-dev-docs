# xmlString

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the string representation of the receiver as it would appear in an XML document.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var xmlString: String { get }
```

```objc
@property (copy, readonly) NSString * XMLString;
```

#### Discussion

The returned string includes the string representations of all children. This method invokes [`xmlString(options:)`](./xmlstring%28options%29.md) with an `options` argument of `NSXMLNodeOptionsNone`.

## See Also

### Emitting Node Content
- [func xmlString(options: XMLNode.Options) -> String](./xmlstring%28options%29.md)
  Returns the string representation of the receiver as it would appear in an XML document, with one or more output options specified.
- [func canonicalXMLStringPreservingComments(Bool) -> String](./canonicalxmlstringpreservingcomments%28_%29.md)
  Returns a string object encapsulating the receiver’s XML in canonical form.
- [var description: String](./description.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/xmlstring)*