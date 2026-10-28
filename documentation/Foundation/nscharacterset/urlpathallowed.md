# urlPathAllowed

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Returns the character set for characters allowed in a path URL component.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var urlPathAllowed: CharacterSet { get }
```

```objc
@property (class, copy, readonly) NSCharacterSet * URLPathAllowedCharacterSet;
```

## Discussion

The path component of a URL is the component immediately following the host component (if present). It ends wherever the query or fragment component begins. For example, in the URL `http://www.example.com/index.php?key1=value1`, the path component is `/index.php`.

## See Also

### Getting Character Sets for URL Encoding
- [class var urlFragmentAllowed: CharacterSet](./urlfragmentallowed.md)
  Returns the character set for characters allowed in a fragment URL component.
- [class var urlHostAllowed: CharacterSet](./urlhostallowed.md)
  Returns the character set for characters allowed in a host URL subcomponent.
- [class var urlPasswordAllowed: CharacterSet](./urlpasswordallowed.md)
  Returns the character set for characters allowed in a password URL subcomponent.
- [class var urlQueryAllowed: CharacterSet](./urlqueryallowed.md)
  Returns the character set for characters allowed in a query URL component.
- [class var urlUserAllowed: CharacterSet](./urluserallowed.md)
  Returns the character set for characters allowed in a user URL subcomponent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/urlpathallowed)*