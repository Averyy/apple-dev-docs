# errSecCSDBAccess

**Framework**: Security  
**Kind**: var

Cannot access signature database.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var errSecCSDBAccess: OSStatus { get }
```

#### Discussion

This error is returned when the system is attempting to sign unsigned code ad-hoc and couldn’t write to the signature database because of some problem other than a permission problem. For example, the signature database might be missing or corrupted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errseccsdbaccess)*