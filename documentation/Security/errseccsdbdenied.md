# errSecCSDBDenied

**Framework**: Security  
**Kind**: var

Access to signature database denied.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var errSecCSDBDenied: OSStatus { get }
```

#### Database

This error is returned when the system is attempting to sign unsigned code ad-hoc and couldn’t write to the signature database because of a permission problem.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/errseccsdbdenied)*