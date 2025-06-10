# prefix

**Framework**: Foundation  
**Kind**: property

Returns the prefix of the receiver’s name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var prefix: String? { get }
```

#### Return Value

A string containing the receiver’s prefix. This method returns an empty string if the receiver’s name is not qualified by a namespace.

#### Discussion

The prefix is the part of a namespace-qualified name that precedes the colon. For example, “acme” is the prefix in the qualified name “acme:chapter”.

## See Also

- [var localName: String?](xmlnode/localname.md)
  Returns the local name of the receiver.
- [class func localName(forName: String) -> String](xmlnode/localname(forname:).md)
  Returns the local name from the specified qualified name.
- [class func prefix(forName: String) -> String?](xmlnode/prefix(forname:).md)
  Returns the prefix from the specified qualified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/prefix)*