# DispatchQueue.AutoreleaseFrequency.workItem

**Framework**: Dispatch  
**Kind**: case

The queue configures an autorelease pool before the execution of a block, and releases the objects in that pool after the block finishes executing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
case workItem
```

## See Also

- [DispatchQueue.AutoreleaseFrequency.inherit](dispatchqueue/autoreleasefrequency/inherit.md)
  The queue inherits its autorelease frequency from its target queue.
- [DispatchQueue.AutoreleaseFrequency.never](dispatchqueue/autoreleasefrequency/never.md)
  The queue does not set up an autorelease pool around executed blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/autoreleasefrequency/workitem)*