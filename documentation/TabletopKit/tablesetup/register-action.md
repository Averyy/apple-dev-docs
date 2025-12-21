# register(action:)

**Framework**: TabletopKit  
**Kind**: method

Register a custom action of given type. Each type of custom action needs to be registered before it can be used.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
mutating func register<Action>(action type: Action.Type) where Action : BitwiseCopyable, Action : CustomAction
```

## Parameters

- `type`: The type of the custom action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tablesetup/register(action:))*