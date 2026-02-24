# addTarget(_:action:)

**Framework**: UIKit  
**Kind**: method

Adds a target and an action to a gesture-recognizer object.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func addTarget(_ target: Any, action: Selector)
```

#### Discussion

You may call this method multiple times to specify multiple target-action pairs. However, if you request to add a target-action pair that has already been added, then the request is ignored.

## Parameters

- `target`: An object that is a recipient of action messages sent by the receiver when the represented gesture occurs. `nil` is not a valid value.
- `action`: A selector identifying a method of a target to be invoked by the action message. `NULL` is not a valid value.

## See Also

- [init(target: Any?, action: Selector?)](uigesturerecognizer/init(target:action:).md)
  Creates a gesture recognizer with a target and an action selector.
- [func removeTarget(Any?, action: Selector?)](uigesturerecognizer/removetarget(_:action:).md)
  Removes a target and an action from a gesture-recognizer object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/addtarget(_:action:))*