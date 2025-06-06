# urlFragmentAllowed

**Framework**: Foundation  
**Kind**: property

Returns the character set for characters allowed in a fragment URL component.

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
class var urlFragmentAllowed: CharacterSet { get }
```

#### Discussion

The fragment component of a URL is the component after a `#` symbol. For example, in the URL `http://www.example.com/index.html#jumpLocation`, the fragment is `jumpLocation`.

## See Also

- [class var urlHostAllowed: CharacterSet](nscharacterset/urlhostallowed.md)
  Returns the character set for characters allowed in a host URL subcomponent.
- [class var urlPasswordAllowed: CharacterSet](nscharacterset/urlpasswordallowed.md)
  Returns the character set for characters allowed in a password URL subcomponent.
- [class var urlPathAllowed: CharacterSet](nscharacterset/urlpathallowed.md)
  Returns the character set for characters allowed in a path URL component.
- [class var urlQueryAllowed: CharacterSet](nscharacterset/urlqueryallowed.md)
  Returns the character set for characters allowed in a query URL component.
- [class var urlUserAllowed: CharacterSet](nscharacterset/urluserallowed.md)
  Returns the character set for characters allowed in a user URL subcomponent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/urlfragmentallowed)*