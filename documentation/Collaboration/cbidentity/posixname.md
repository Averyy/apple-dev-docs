# posixName

**Framework**: Collaboration  
**Kind**: property

Returns the POSIX name of the identity.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var posixName: String { get }
```

#### Return Value

The POSIX name of the identity.

#### Discussion

The POSIX name is also referred to as the “short name” for an identity. It can only contain the characters A-Z, a-z, 0-9, -, _, ., and @.

## See Also

- [var aliases: [String]](cbidentity/aliases.md)
  Returns an array of aliases (alternate names) for the identity.
- [var authority: CBIdentityAuthority](cbidentity/authority.md)
  Returns the identity authority where the identity is stored.
- [var emailAddress: String?](cbidentity/emailaddress.md)
  Returns the email address of an identity.
- [var fullName: String](cbidentity/fullname.md)
  Returns the full name of the identity.
- [var image: NSImage?](cbidentity/image.md)
  Returns the image associated with an identity.
- [var isHidden: Bool](cbidentity/ishidden.md)
  Returns a Boolean value indicating the state of the identity’s hidden property.
- [func isMember(ofGroup: CBGroupIdentity) -> Bool](cbidentity/ismember(ofgroup:).md)
  Returns a Boolean value indicating whether the identity is a member of the specified group.
- [var uuidString: String](cbidentity/uuidstring.md)
  Returns the UUID of the identity as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/posixname)*