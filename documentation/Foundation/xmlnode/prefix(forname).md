# prefix(forName:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the prefix from the specified qualified name.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func prefix(forName name: String) -> String?
```

```objc
+ (NSString *) prefixForName:(NSString *) name;
```

## Discussion

For example, if the qualified name is “bst:title”, this method returns “bst”.

## Parameters

- `name`: A string that is a qualified name.

## See Also

### Related Documentation
- [class func predefinedNamespace(forPrefix: String) -> XMLNode?](./predefinednamespace%28forprefix%29.md)
  Returns an `NSXMLNode` object representing one of the predefined namespaces with the specified prefix.
### Managing Namespaces
- [var localName: String?](./localname.md)
  Returns the local name of the receiver.
- [class func localName(forName: String) -> String](./localname%28forname%29.md)
  Returns the local name from the specified qualified name.
- [var prefix: String?](./prefix.md)
  Returns the prefix of the receiver’s name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xmlnode/prefix(forname:))*