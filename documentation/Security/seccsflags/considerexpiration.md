# considerExpiration

**Framework**: Security  
**Kind**: property

Consider expired certificates invalid.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
static var considerExpiration: SecCSFlags { get }
```

#### Discussion

When passed to a function that performs code validation, this flag requests that code signatures made by expired certificates be rejected. By default, expiration of participating certificates is not automatic grounds for rejection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccsflags/considerexpiration)*