# uuidString

**Framework**: Collaboration  
**Kind**: property  
**Role**: Instance Property

Returns the UUID of the identity as a string.

**Availability**:
- macOS 10.5+ - Deprecated in 10.11

> **Deprecated**: Use the uniqueIdentifier property instead.

## Declaration

```swift
var uuidString: String { get }
```

```objc
@property (nonatomic, readonly) NSString * UUIDString;
```

#### Return Value

The UUID string of the identity.

#### Discussion

The UUID string is generated so it is unique across all identity authorities. When storing ACLs, one method is to store the UUID of each identity. However, it is recommended that you use a persistent data object instead (see [`persistentReference`](./persistentreference.md)).

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
- [func isMember(ofGroup: CBGroupIdentity) -> Bool](./ismember%28ofgroup%29.md)
  Returns a Boolean value indicating whether the identity is a member of the specified group.
- [var posixName: String](./posixname.md)
  Returns the POSIX name of the identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/uuidstring)*