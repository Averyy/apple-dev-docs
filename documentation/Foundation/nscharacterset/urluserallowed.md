# urlUserAllowed

**Framework**: Foundation  
**Kind**: property

Returns the character set for characters allowed in a user URL subcomponent.

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
class var urlUserAllowed: CharacterSet { get }
```

#### Discussion

The user component of a URL is an optional component that precedes the host component, and ends at either a colon (if a password is specified) or an `@` sign (if no password is specified). For example, in the URL `http://username:password@www.example.com/index.html`, the user component is `username`.

## See Also

- [class var urlFragmentAllowed: CharacterSet](nscharacterset/urlfragmentallowed.md)
  Returns the character set for characters allowed in a fragment URL component.
- [class var urlHostAllowed: CharacterSet](nscharacterset/urlhostallowed.md)
  Returns the character set for characters allowed in a host URL subcomponent.
- [class var urlPasswordAllowed: CharacterSet](nscharacterset/urlpasswordallowed.md)
  Returns the character set for characters allowed in a password URL subcomponent.
- [class var urlPathAllowed: CharacterSet](nscharacterset/urlpathallowed.md)
  Returns the character set for characters allowed in a path URL component.
- [class var urlQueryAllowed: CharacterSet](nscharacterset/urlqueryallowed.md)
  Returns the character set for characters allowed in a query URL component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/urluserallowed)*