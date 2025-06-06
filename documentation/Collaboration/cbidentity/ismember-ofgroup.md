# isMember(ofGroup:)

**Framework**: Collaboration  
**Kind**: method

Returns a Boolean value indicating whether the identity is a member of the specified group.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func isMember(ofGroup group: CBGroupIdentity) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the identity is a member of the group; [`false`](https://developer.apple.com/documentation/swift/false) if it is not.

## Parameters

- `group`: The group to check for membership.

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
- [var posixName: String](cbidentity/posixname.md)
  Returns the POSIX name of the identity.
- [var uuidString: String](cbidentity/uuidstring.md)
  Returns the UUID of the identity as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/ismember(ofgroup:))*