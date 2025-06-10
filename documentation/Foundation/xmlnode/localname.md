# localName

**Framework**: Foundation  
**Kind**: property

Returns the local name of the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var localName: String? { get }
```

#### Return Value

A string containing the local name of the receiver.

#### Discussion

The local name is the part of a node name that follows a namespace-qualifying colon or the full name if there is no colon. For example, “chapter” is the local name in the qualified name “acme:chapter”.

## See Also

- [class func localName(forName: String) -> String](xmlnode/localname(forname:).md)
  Returns the local name from the specified qualified name.
- [var prefix: String?](xmlnode/prefix.md)
  Returns the prefix of the receiver’s name.
- [class func prefix(forName: String) -> String?](xmlnode/prefix(forname:).md)
  Returns the prefix from the specified qualified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/localname)*