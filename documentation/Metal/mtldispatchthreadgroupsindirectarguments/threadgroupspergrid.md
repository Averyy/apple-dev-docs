# threadgroupsPerGrid

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The number of threadgroups for the grid, in each dimension.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
var threadgroupsPerGrid: (UInt32, UInt32, UInt32)
```

```c
uint32_t threadgroupsPerGrid[3];
```

## See Also

### Specifying the size of the threadgroup
- [init()](./init%28%29.md)
  Returns a new data layout for dispatching threadgroups over indirect buffer calls.
- [init(threadgroupsPerGrid: (UInt32, UInt32, UInt32))](./init%28threadgroupspergrid%29.md)
  Returns a new data layout for dispatching threadgroups over indirect buffer calls, with specified threadgroups per grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldispatchthreadgroupsindirectarguments/threadgroupspergrid)*