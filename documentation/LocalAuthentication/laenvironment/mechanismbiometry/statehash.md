# stateHash

**Framework**: Local Authentication  
**Kind**: property

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var stateHash: Data { get }
```

#### Discussion

This value represents the state of the enrollment and changes whenever the biometric enrollment is changed. It does not directly map to the enrolled templates, e.g. if a finger is added to Touch ID enrollement and then removed, the final state would be different. It also returns different values to different apps to prevent tracking of user identity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/mechanismbiometry/statehash)*