# userPassword

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
var userPassword: LAEnvironment.MechanismUserPassword? { get }
```

#### Discussion

Information about local user password (on macOS) or passcode (on embedded platforms).

@c nil if user password or passcode is not supported by this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laenvironment/state-swift.class/userpassword)*