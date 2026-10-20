# urlHostAllowed

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Returns the character set for characters allowed in a host URL subcomponent.

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
class var urlHostAllowed: CharacterSet { get }
```

```objc
@property (class, copy, readonly) NSCharacterSet * URLHostAllowedCharacterSet;
```

#### Discussion

The host component of a URL is usually the component immediately after the first two leading slashes. If the URL contains a username and password, the host component is the component after the `@` sign. For example, in the URL `http://username:password@www.example.com/index.html`, the host component is `www.example.com`.

## See Also

### Getting Character Sets for URL Encoding
- [class var urlFragmentAllowed: CharacterSet](./urlfragmentallowed.md)
  Returns the character set for characters allowed in a fragment URL component.
- [class var urlPasswordAllowed: CharacterSet](./urlpasswordallowed.md)
  Returns the character set for characters allowed in a password URL subcomponent.
- [class var urlPathAllowed: CharacterSet](./urlpathallowed.md)
  Returns the character set for characters allowed in a path URL component.
- [class var urlQueryAllowed: CharacterSet](./urlqueryallowed.md)
  Returns the character set for characters allowed in a query URL component.
- [class var urlUserAllowed: CharacterSet](./urluserallowed.md)
  Returns the character set for characters allowed in a user URL subcomponent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/urlhostallowed)*