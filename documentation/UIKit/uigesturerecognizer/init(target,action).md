# init(target:action:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a gesture recognizer with a target and an action selector.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(target: Any?, action: Selector?)
```

```objc
- (instancetype) initWithTarget:(id) target action:(SEL) action;
```

## Return Value

An initialized instance of a concrete [`UIGestureRecognizer`](../uigesturerecognizer.md) subclass.

## Discussion

This method is the designated initializer. After creating the gesture recognizer, you may associate other target-action pairs with it by calling [`addTarget(_:action:)`](./addtarget%28_,action%29.md).

## Parameters

- `target`: An object that is the recipient of action messages sent by the receiver when it recognizes a gesture. `nil` isn’t a valid value.
- `action`: A selector that identifies the method implemented by the target to handle the gesture recognized by the receiver. The action selector must conform to the signature described in the class overview. `nil` isn’t a valid value.

## See Also

### Related Documentation
- [func removeTarget(Any?, action: Selector?)](./removetarget%28_,action%29.md)
  Removes a target and an action from a gesture-recognizer object.
- [func addTarget(Any, action: Selector)](./addtarget%28_,action%29.md)
  Adds a target and an action to a gesture-recognizer object.
### Initializing a gesture recognizer
- [convenience init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a gesture recognizer from data in an unarchiver.
- [convenience init()](./init%28%29.md)
  Creates a gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/init(target:action:))*