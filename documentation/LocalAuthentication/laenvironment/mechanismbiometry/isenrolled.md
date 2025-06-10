# isEnrolled

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
var isEnrolled: Bool { get }
```

#### Discussion

Even if biometry is enrolled, it does not necessarily mean that it can be used. You should check @c isUsable property to see if it is available for use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/mechanismbiometry/isenrolled)*