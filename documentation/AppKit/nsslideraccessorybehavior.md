# NSSliderAccessoryBehavior

**Framework**: AppKit  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12+

## Declaration

```swift
@MainActor
class NSSliderAccessoryBehavior
```

## Topics

### Initializers
- [init(handler: (NSSliderAccessory) -> Void)](nsslideraccessorybehavior/init(handler:).md)
  The handler block is invoked on interaction.
- [init(target: Any?, action: Selector)](nsslideraccessorybehavior/init(target:action:).md)
  The action is sent to the target on interaction.
### Type Properties
- [class var automatic: NSSliderAccessoryBehavior](nsslideraccessorybehavior/automatic.md)
  The behavior is automatically picked to be the system standard, given the slider’s current context.
- [class var valueReset: NSSliderAccessoryBehavior](nsslideraccessorybehavior/valuereset.md)
  The value of the slider is reset to the associated value for the accessory.
- [class var valueStep: NSSliderAccessoryBehavior](nsslideraccessorybehavior/valuestep.md)
  The value of the slider moves towards the associated value for the accessory with by a delta of the slider’s `altIncrementValue`.
### Instance Methods
- [func handleAction(NSSliderAccessory)](nsslideraccessorybehavior/handleaction(_:).md)
  Override point for custom subclasses to handle interaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSSliderAccessory](nsslideraccessory.md)
- [NSSliderAccessory.Width](nsslideraccessory/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslideraccessorybehavior)*