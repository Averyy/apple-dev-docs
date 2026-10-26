# current

**Framework**: Game Controller  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, atomic, strong, readonly, nullable) GCController * current;
```

#### Discussion

Use this property for a single-player game when you don’t need to distinguish the input from multiple controllers simultaneously.

## See Also

### Handling multiple controllers
- [static let GCControllerDidBecomeCurrent: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gccontrollerdidbecomecurrent.md)
  A notification that posts when a controller becomes the current controller.
- [static let GCControllerDidStopBeingCurrent: NSNotification.Name](../../Foundation/nsnotification/name-swift.struct/gccontrollerdidstopbeingcurrent.md)
  A notification that posts when a controller stops being the current controller.
- [GCControllerDidBecomeCurrentNotification](../gccontrollerdidbecomecurrentnotification.md)
  A notification that posts when a controller becomes the current controller.
- [GCControllerDidStopBeingCurrentNotification](../gccontrollerdidstopbeingcurrentnotification.md)
  A notification that posts when a controller stops being the current controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/current)*