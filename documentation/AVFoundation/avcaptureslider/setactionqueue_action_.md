# setActionQueue:action:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the action to perform on the specified dispatch queue when the slider’s value changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```objc
- (void) setActionQueue:(dispatch_queue_t) actionQueue action:(void (^)(float newValue)) action;
```

## Discussion

If the action modifies a property of the camera system, the specified dispatch queue must represent the camera system’s same exclusive execution context (see [`isSameExclusiveExecutionContext(other:)`](../../Swift/serialexecutor/issameexclusiveexecutioncontext%28other%29.md)).

## Parameters

- `actionQueue`: A dispatch queue on which to call the action.
- `action`: The action to perform in response to changes to the slider’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider/setactionqueue:action:)*