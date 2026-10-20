# xmlData

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var xmlData: Data { get }
```

```objc
@property (copy, readonly) NSData * XMLData;
```

#### Discussion

This method invokes [`xmlData(options:)`](./xmldata%28options%29.md) with an option of `NSXMLNodeOptionsNone`. The encoding used is based on the value returned from [`characterEncoding`](./characterencoding.md) or UTF-8 if no valid encoding is returned by that method.

## See Also

### Writing a Document as XML Data
- [func xmlData(options: XMLNode.Options) -> Data](./xmldata%28options%29.md)
  Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/xmldata)*