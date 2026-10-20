# posixGID

**Framework**: Collaboration  
**Kind**: property  
**Role**: Instance Property

Returns the POSIX GID of the identity.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var posixGID: gid_t { get }
```

```objc
@property (nonatomic, readonly) gid_t posixGID;
```

#### Return Value

The POSIX GID of the group identity.

#### Discussion

The POSIX GID is an integer that can identify a group within an identity authority. GIDs are not guaranteed to be unique within an identity authority.


---

*[View on Apple Developer](https://developer.apple.com/documentation/collaboration/cbgroupidentity/posixgid)*