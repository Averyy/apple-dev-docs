# extendRights

**Framework**: Security  
**Kind**: property

A flag that permits the Security Server to attempt to grant the rights requested.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var extendRights: AuthorizationFlags { get }
```

#### Discussion

Once the Security Server denies one right, it ignores the remaining requested rights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationflags/extendrights)*