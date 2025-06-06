# rangeOfPassword

**Framework**: Foundation  
**Kind**: property

Returns the character range of the password in the string returned by the string property.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var rangeOfPassword: Range<String.Index>? { get }
```

#### Discussion

If the component does not exist, nil is returned.

> **Note**:  Zero length components are legal. For example, the URL string “scheme://:@/?#” has a zero length user, password, host, query and fragment; the URL strings “scheme:” and “” both have a zero length path.

 Zero length components are legal. For example, the URL string “scheme://:@/?#” has a zero length user, password, host, query and fragment; the URL strings “scheme:” and “” both have a zero length path.

## See Also

- [var rangeOfFragment: Range<String.Index>?](urlcomponents/rangeoffragment.md)
  Returns the character range of the fragment in the string returned by the string property.
- [var rangeOfHost: Range<String.Index>?](urlcomponents/rangeofhost.md)
  Returns the character range of the host in the string returned by the string property.
- [var rangeOfPath: Range<String.Index>?](urlcomponents/rangeofpath.md)
  Returns the character range of the path in the string returned by the string property.
- [var rangeOfPort: Range<String.Index>?](urlcomponents/rangeofport.md)
  Returns the character range of the port in the string returned by the string property.
- [var rangeOfQuery: Range<String.Index>?](urlcomponents/rangeofquery.md)
  Returns the character range of the query in the string returned by the string property.
- [var rangeOfScheme: Range<String.Index>?](urlcomponents/rangeofscheme.md)
  Returns the character range of the scheme in the string returned by the string property.
- [var rangeOfUser: Range<String.Index>?](urlcomponents/rangeofuser.md)
  Returns the character range of the user in the string returned by the string property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlcomponents/rangeofpassword)*