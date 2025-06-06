# removeActionSet(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Removes an action set from the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func removeActionSet(_ actionSet: HMActionSet) async throws
```

## Parameters

- `actionSet`: The action set to remove.
- `completion`: The block executed after the request is processed.

## See Also

- [var actionSets: [HMActionSet]](hmtrigger/actionsets.md)
  Array of all action sets that will be executed by the trigger.
- [func addActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](hmtrigger/addactionset(_:completionhandler:).md)
  Adds an action set to the trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/removeactionset(_:completionhandler:))*