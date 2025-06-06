# current

**Framework**: Game Controller  
**Kind**: property

The most recently used game controller.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class var current: GCController? { get }
```

#### Discussion

Use this property for a single-player game when you don’t need to distinguish the input from multiple controllers simultaneously.

## See Also

- [static let GCControllerDidBecomeCurrent: NSNotification.Name](../foundation/nsnotification/name/3547191-gccontrollerdidbecomecurrent.md)
  A notification that posts when a controller becomes the current controller.
- [static let GCControllerDidStopBeingCurrent: NSNotification.Name](../foundation/nsnotification/name/3547192-gccontrollerdidstopbeingcurrent.md)
  A notification that posts when a controller stops being the current controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/current)*