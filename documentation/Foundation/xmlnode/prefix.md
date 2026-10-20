# prefix

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the prefix of the receiver’s name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var prefix: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * prefix;
```

#### Return Value

A string containing the receiver’s prefix. This method returns an empty string if the receiver’s name is not qualified by a namespace.

#### Discussion

The prefix is the part of a namespace-qualified name that precedes the colon. For example, “acme” is the prefix in the qualified name “acme:chapter”.

## See Also

### Managing Namespaces
- [var localName: String?](./localname.md)
  Returns the local name of the receiver.
- [class func localName(forName: String) -> String](./localname%28forname%29.md)
  Returns the local name from the specified qualified name.
- [class func prefix(forName: String) -> String?](./prefix%28forname%29.md)
  Returns the prefix from the specified qualified name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/prefix)*