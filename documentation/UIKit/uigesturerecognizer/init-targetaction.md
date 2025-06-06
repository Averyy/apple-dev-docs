# init(target:action:)

**Framework**: UIKit  
**Kind**: init

Creates a gesture recognizer with a target and an action selector.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(target: Any?, action: Selector?)
```

#### Return Value

An initialized instance of a concrete [`UIGestureRecognizer`](uigesturerecognizer.md) subclass.

#### Discussion

This method is the designated initializer. After creating the gesture recognizer, you may associate other target-action pairs with it by calling [`addTarget(_:action:)`](uigesturerecognizer/addtarget(_:action:).md).

## Parameters

- `target`: An object that is the recipient of action messages sent by the receiver when it recognizes a gesture.   isn’t a valid value.
- `action`: A selector that identifies the method implemented by the target to handle the gesture recognized by the receiver. The action selector must conform to the signature described in the class overview.   isn’t a valid value.

## See Also

- [func removeTarget(Any?, action: Selector?)](uigesturerecognizer/removetarget(_:action:).md)
  Removes a target and an action from a gesture-recognizer object.
- [func addTarget(Any, action: Selector)](uigesturerecognizer/addtarget(_:action:).md)
  Adds a target and an action to a gesture-recognizer object.
- [convenience init?(coder: NSCoder)](uigesturerecognizer/init(coder:).md)
  Creates a gesture recognizer from data in an unarchiver.
- [convenience init()](uigesturerecognizer/init.md)
  Creates a gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/init(target:action:))*