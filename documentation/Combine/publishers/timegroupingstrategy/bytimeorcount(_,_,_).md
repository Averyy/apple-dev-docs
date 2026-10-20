# Publishers.TimeGroupingStrategy.byTimeOrCount(_:_:_:)

**Framework**: Combine  
**Kind**: case  
**Role**: Case

A grouping that collects and publishes items periodically or when a buffer reaches a maximum size.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case byTimeOrCount(Context, Context.SchedulerTimeType.Stride, Int)
```

## See Also

### Time groupings
- [case byTime(Context, Context.SchedulerTimeType.Stride)](./bytime%28_,_%29.md)
  A grouping that collects and periodically publishes items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/timegroupingstrategy/bytimeorcount(_:_:_:))*