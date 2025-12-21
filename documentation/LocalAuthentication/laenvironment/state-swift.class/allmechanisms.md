# allMechanisms

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
var allMechanisms: [LAEnvironment.Mechanism] { get }
```

#### Discussion

Information about all authentication mechanisms.

This property aggregates @c biometry, @c userPassword, @c companions and any future authentication mechanisms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/state-swift.class/allmechanisms)*