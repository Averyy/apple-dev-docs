# delegate

**Framework**: AVKit  
**Kind**: property

A delegate object for the experience controller.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
weak final var delegate: (any AVExperienceController.Delegate)? { get set }
```

#### Discussion

Provide a delegate to have the system notify your app about transitions and other state changes. Use the delegate callbacks to update your app’s state and user interface in response.

## See Also

- [AVExperienceController.Delegate](avexperiencecontroller/delegate-swift.protocol.md)
  A protocol that defines the methods to implement to respond to experience changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avexperiencecontroller/delegate-swift.property)*