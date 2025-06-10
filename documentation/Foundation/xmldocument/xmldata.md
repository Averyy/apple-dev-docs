# xmlData

**Framework**: Foundation  
**Kind**: property

Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var xmlData: Data { get }
```

#### Discussion

This method invokes [`xmlData(options:)`](xmldocument/xmldata(options:).md) with an option of `NSXMLNodeOptionsNone`. The encoding used is based on the value returned from [`characterEncoding`](xmldocument/characterencoding.md) or UTF-8 if no valid encoding is returned by that method.

## See Also

- [func xmlData(options: XMLNode.Options) -> Data](xmldocument/xmldata(options:).md)
  Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/xmldata)*