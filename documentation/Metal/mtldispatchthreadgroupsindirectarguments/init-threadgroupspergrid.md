# init(threadgroupsPerGrid:)

**Framework**: Metal  
**Kind**: init

Returns a new data layout for dispatching threadgroups over indirect buffer calls, with specified threadgroups per grid.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init(threadgroupsPerGrid: (UInt32, UInt32, UInt32))
```

## Parameters

- `threadgroupsPerGrid`: The number of threadgroups for the grid, in each dimension.

## See Also

- [init()](mtldispatchthreadgroupsindirectarguments/init.md)
  Returns a new data layout for dispatching threadgroups over indirect buffer calls.
- [var threadgroupsPerGrid: (UInt32, UInt32, UInt32)](mtldispatchthreadgroupsindirectarguments/threadgroupspergrid.md)
  The number of threadgroups for the grid, in each dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldispatchthreadgroupsindirectarguments/init(threadgroupspergrid:))*