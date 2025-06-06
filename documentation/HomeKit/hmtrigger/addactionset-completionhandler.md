# addActionSet(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Adds an action set to the trigger.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func addActionSet(_ actionSet: HMActionSet) async throws
```

## Parameters

- `actionSet`: The new action set.
- `completion`: The block executed after the request is processed.

## See Also

- [var actionSets: [HMActionSet]](hmtrigger/actionsets.md)
  Array of all action sets that will be executed by the trigger.
- [func removeActionSet(HMActionSet, completionHandler: ((any Error)?) -> Void)](hmtrigger/removeactionset(_:completionhandler:).md)
  Removes an action set from the trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmtrigger/addactionset(_:completionhandler:))*