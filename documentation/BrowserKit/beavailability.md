# BEAvailability

**Framework**: BrowserKit  
**Kind**: class

A class that tests whether a device is eligible to run an alternative browser engine.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
class BEAvailability
```

## Topics

### Testing eligibility
- [class func isEligible(for: BEAvailability.Context, completionHandler: (Bool, (any Error)?) -> Void)](beavailability/iseligible(for:completionhandler:).md)
  Tests whether the device is eligible to use an app that contains an alternative browser engine.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [BEAvailability.Context](beavailability/context.md)
  The category of app for which you determine eligibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beavailability)*