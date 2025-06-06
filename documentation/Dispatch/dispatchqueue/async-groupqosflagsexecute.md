# async(group:qos:flags:execute:)

**Framework**: Dispatch  
**Kind**: method

Schedules a block asynchronously for execution and optionally associates it with a dispatch group.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@preconcurrency
func async(group: DispatchGroup? = nil, qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], execute work: @escaping () -> Void)
```

## Parameters

- `group`: The dispatch group to associate with the work item. If you specify  , the block is not associated with a group.
- `qos`: The quality-of-service class to use when executing the block. This parameter determines the priority with which the block is scheduled and executed. For a list of possible values, see  .
- `flags`: Additional attributes to apply when executing the block. For a list of possible values, see  .
- `work`: The block containing the work to perform. This block has no return value and no parameters.

## See Also

- [func async(group: DispatchGroup, execute: DispatchWorkItem)](dispatchqueue/async(group:execute:).md)
  Schedules a work item asynchronously for execution and associates it with the specified dispatch group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/async(group:qos:flags:execute:))*