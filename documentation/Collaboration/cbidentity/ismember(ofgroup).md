# isMember(ofGroup:)

**Framework**: Collaboration  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the identity is a member of the specified group.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func isMember(ofGroup group: CBGroupIdentity) -> Bool
```

```objc
- (BOOL) isMemberOfGroup:(CBGroupIdentity *) group;
```

## Return Value

[`true`](../../Swift/true.md) if the identity is a member of the group; [`false`](../../Swift/false.md) if it is not.

## Parameters

- `group`: The group to check for membership.

## See Also

### Getting Identity Attributes
- [var aliases: [String]](./aliases.md)
  Returns an array of aliases (alternate names) for the identity.
- [var authority: CBIdentityAuthority](./authority.md)
  Returns the identity authority where the identity is stored.
- [var emailAddress: String?](./emailaddress.md)
  Returns the email address of an identity.
- [var fullName: String](./fullname.md)
  Returns the full name of the identity.
- [var image: NSImage?](./image.md)
  Returns the image associated with an identity.
- [var isHidden: Bool](./ishidden.md)
  Returns a Boolean value indicating the state of the identity’s hidden property.
- [var posixName: String](./posixname.md)
  Returns the POSIX name of the identity.
- [var uuidString: String](./uuidstring.md)
  Returns the UUID of the identity as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/ismember(ofgroup:))*