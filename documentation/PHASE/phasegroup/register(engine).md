# register(engine:)

**Framework**: PHASE  
**Kind**: method

Adds the group to the engine’s dictionary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func register(engine: PHASEEngine)
```

#### Discussion

The function generates an exception if the argument is `nil` or if engine already contains the group. For more information, see [`groups`](phaseengine/groups.md).

## Parameters

- `engine`: The engine with which to register this group.

## See Also

- [func unregisterFromEngine()](phasegroup/unregisterfromengine.md)
  Removes the group from the engine’s dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegroup/register(engine:))*