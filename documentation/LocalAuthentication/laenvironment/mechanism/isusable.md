# isUsable

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
var isUsable: Bool { get }
```

#### Discussion

Whether the mechanism is available for use, i.e. whether the relevant preflight call of @c canEvaluatePolicy would succeed.

properties of the subclass to determine why mechanism can’t be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/mechanism/isusable)*