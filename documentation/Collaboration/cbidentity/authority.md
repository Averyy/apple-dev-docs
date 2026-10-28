# authority

**Framework**: Collaboration  
**Kind**: property  
**Role**: Instance Property

Returns the identity authority where the identity is stored.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var authority: CBIdentityAuthority { get }
```

```objc
@property (nonatomic, readonly) CBIdentityAuthority * authority;
```

## Return Value

The identity authority where the identity is stored.

## See Also

### Getting Identity Attributes
- [var aliases: [String]](./aliases.md)
  Returns an array of aliases (alternate names) for the identity.
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
- [var uuidString: String](./uuidstring.md)
  Returns the UUID of the identity as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbidentity/authority)*