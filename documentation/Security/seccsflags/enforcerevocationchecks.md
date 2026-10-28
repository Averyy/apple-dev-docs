# enforceRevocationChecks

**Framework**: Security  
**Kind**: property  
**Role**: Type Property

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var enforceRevocationChecks: SecCSFlags { get }
```

```c
kSecCSEnforceRevocationChecks
```

## Discussion

Forces checking of certificates against revocation lists or OCSP (online certificate status protocol) regardless of preference settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccsflags/enforcerevocationchecks)*