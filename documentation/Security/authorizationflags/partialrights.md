# partialRights

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

A flag that permits the Security Server to grant rights on an individual basis.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var partialRights: AuthorizationFlags { get }
```

```c
kAuthorizationFlagPartialRights
```

#### Discussion

If this and the [`extendRights`](./extendrights.md) flags are set, the Security Server grants or denies rights on an individual basis and all rights are checked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationflags/partialrights)*