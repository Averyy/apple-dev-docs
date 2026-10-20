# NSSliderAccessoryBehavior

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSSliderAccessoryBehavior : NSObject
```

## Topics

### Initializers
- [init(handler: (NSSliderAccessory) -> Void)](./nsslideraccessorybehavior/init%28handler%29.md)
  The handler block is invoked on interaction.
- [init(target: Any?, action: Selector)](./nsslideraccessorybehavior/init%28target,action%29.md)
  The action is sent to the target on interaction.
- [init?(coder: NSCoder)](./nsslideraccessorybehavior/init%28coder%29.md)
### Type Properties
- [class var automatic: NSSliderAccessoryBehavior](./nsslideraccessorybehavior/automatic.md)
  The behavior is automatically picked to be the system standard, given the slider’s current context.
- [class var valueReset: NSSliderAccessoryBehavior](./nsslideraccessorybehavior/valuereset.md)
  The value of the slider is reset to the associated value for the accessory.
- [class var valueStep: NSSliderAccessoryBehavior](./nsslideraccessorybehavior/valuestep.md)
  The value of the slider moves towards the associated value for the accessory with by a delta of the slider’s `altIncrementValue`.
### Instance Methods
- [func handleAction(NSSliderAccessory)](./nsslideraccessorybehavior/handleaction%28_%29.md)
  Override point for custom subclasses to handle interaction.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Accessories
- [class NSSliderAccessory](./nsslideraccessory.md)
- [NSSliderAccessory.Width](./nsslideraccessory/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslideraccessorybehavior)*