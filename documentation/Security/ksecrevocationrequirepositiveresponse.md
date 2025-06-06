# kSecRevocationRequirePositiveResponse

**Framework**: Security  
**Kind**: var

Require a positive response to pass the policy.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var kSecRevocationRequirePositiveResponse: CFOptionFlags { get }
```

#### Discussion

If the flag is not set, revocation checking is done on a “best attempt” basis, where failure to reach the server is not considered fatal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecrevocationrequirepositiveresponse)*