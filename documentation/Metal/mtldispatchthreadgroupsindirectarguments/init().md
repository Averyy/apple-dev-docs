# init()

**Framework**: Metal  
**Kind**: init  
**Role**: Initializer

Returns a new data layout for dispatching threadgroups over indirect buffer calls.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
init()
```

## See Also

### Specifying the size of the threadgroup
- [init(threadgroupsPerGrid: (UInt32, UInt32, UInt32))](./init%28threadgroupspergrid%29.md)
  Returns a new data layout for dispatching threadgroups over indirect buffer calls, with specified threadgroups per grid.
- [var threadgroupsPerGrid: (UInt32, UInt32, UInt32)](./threadgroupspergrid.md)
  The number of threadgroups for the grid, in each dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldispatchthreadgroupsindirectarguments/init())*