# destroyRights

**Framework**: Security  
**Kind**: property

A flag that instructs the Security Server to revoke authorization.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var destroyRights: AuthorizationFlags { get }
```

#### Discussion

If this flag is set, the Security Server revokes authorization from the process as well as from any other process that is sharing the authorization. If not set, the Security Server revokes authorization from the process but not from other processes that share the authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationflags/destroyrights)*