# xmlData(options:)

**Framework**: Foundation  
**Kind**: method

Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func xmlData(options: XMLNode.Options = []) -> Data
```

#### Discussion

The encoding used is based on the value returned from [`characterEncoding`](xmldocument/characterencoding.md).

## Parameters

- `options`: One or more options (bit-OR’d if multiple) to affect the output of the document; see Constants for the valid output options.

## See Also

- [var xmlData: Data](xmldocument/xmldata.md)
  Returns the XML string representation of the receiver—that is, the entire document—encapsulated in a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmldocument/xmldata(options:))*