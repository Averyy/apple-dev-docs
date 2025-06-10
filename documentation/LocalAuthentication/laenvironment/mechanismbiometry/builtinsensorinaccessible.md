# builtInSensorInaccessible

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
var builtInSensorInaccessible: Bool { get }
```

#### Discussion

Currently, the only example of this is a Clamshell Mode on macOS. The user will be not able to use Touch ID if the MacBook lid is closed while connected to external monitor and keyboard, unless the external keyboard has Touch ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/mechanismbiometry/builtinsensorinaccessible)*