# isHidden

**Framework**: Collaboration  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value indicating the state of the identity’s hidden property.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isHidden: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isHidden) BOOL hidden;
```

## Return Value

[`true`](../../Swift/true.md) if the identity is hidden; [`false`](../../Swift/false.md) if it is not.

## Discussion

A hidden identity does not show up in the Identity Picker. A hidden identity refers to system identities such as `root`, `www`, and `wheel`.

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
- [func isMember(ofGroup: CBGroupIdentity) -> Bool](./ismember%28ofgroup%29.md)
  Returns a Boolean value indicating whether the identity is a member of the specified group.
- [var posixName: String](./posixname.md)
  Returns the POSIX name of the identity.
- [var uuidString: String](./uuidstring.md)
  Returns the UUID of the identity as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/ishidden)*