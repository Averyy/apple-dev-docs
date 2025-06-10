# dispatchEvent(name:canBubble:cancellable:extraInfo:completion:)

**Framework**: TVMLKit  
**Kind**: method

Dispatches a custom-named event.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
func dispatchEvent(name eventName: String, canBubble: Bool, cancellable isCancellable: Bool, extraInfo: [String : Any]?) async -> (Bool, Bool)
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func dispatchEvent(name eventName: String, canBubble: Bool, cancellable isCancellable: Bool, extraInfo: [String : Any]?) async -> (Bool, Bool)
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Use this method to dispatch custom-named events from views and view controllers to JavaScript.

## Parameters

- `eventName`: The name of the event.
- `canBubble`: A flag indicating that an event is dispatched on the target’s parent nodes after the event has been dispatched on the target.
- `isCancellable`: A flag indicating whether the event is cancelable.
- `extraInfo`: Extra properties that need to be exposed in the event object.
- `completion`: A block object to be executed when the dispatch call is complete. This block has no return value and takes two Boolean arguments that indicate whether or not the event has been dispatched and whether it was canceled. This parameter may be NULL.

## See Also

- [func dispatchEvent(type: TVElementEventType, canBubble: Bool, cancellable: Bool, extraInfo: [String : Any]?, completion: ((Bool, Bool) -> Void)?)](tvviewelement/dispatchevent(type:canbubble:cancellable:extrainfo:completion:).md)
  Dispatches an event of a specific type to the JavaScript file.
- [enum TVElementEventType](tvelementeventtype.md)
  The type of event that has been dispatched.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvviewelement/dispatchevent(name:canbubble:cancellable:extrainfo:completion:))*