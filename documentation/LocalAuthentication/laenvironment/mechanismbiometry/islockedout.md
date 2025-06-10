# isLockedOut

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
var isLockedOut: Bool { get }
```

#### Discussion

The system might lock the user out of biometry for various reasons. For example, with Face ID, the user is locked out after 5 failed match attempts in row. To recover from bio lockout, users need to enter their passcode (e.g. during device ulock).


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/mechanismbiometry/islockedout)*