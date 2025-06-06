# removeTarget(_:action:)

**Framework**: UIKit  
**Kind**: method

Removes a target and an action from a gesture-recognizer object.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func removeTarget(_ target: Any?, action: Selector?)
```

#### Discussion

Calling this method removes the specified target-action pair. Passing `nil` for `target` matches all targets and passing `NULL` for `action` matches all actions.

## Parameters

- `target`: An object that currently is a recipient of action messages sent by the receiver when the represented gesture occurs. Specify   if you want to remove all targets from the receiver.
- `action`: A selector identifying a method of a target to be invoked by the action message. Specify   if you want to remove all actions from the receiver.

## See Also

- [init(target: Any?, action: Selector?)](uigesturerecognizer/init(target:action:).md)
  Creates a gesture recognizer with a target and an action selector.
- [func addTarget(Any, action: Selector)](uigesturerecognizer/addtarget(_:action:).md)
  Adds a target and an action to a gesture-recognizer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/removetarget(_:action:))*