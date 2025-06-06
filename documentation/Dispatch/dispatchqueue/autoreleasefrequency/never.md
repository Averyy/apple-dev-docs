# DispatchQueue.AutoreleaseFrequency.never

**Framework**: Dispatch  
**Kind**: case

The queue does not set up an autorelease pool around executed blocks.

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
case never
```

#### Discussion

This option is the default behavior for the system-defined global queues.

## See Also

- [DispatchQueue.AutoreleaseFrequency.inherit](dispatchqueue/autoreleasefrequency/inherit.md)
  The queue inherits its autorelease frequency from its target queue.
- [DispatchQueue.AutoreleaseFrequency.workItem](dispatchqueue/autoreleasefrequency/workitem.md)
  The queue configures an autorelease pool before the execution of a block, and releases the objects in that pool after the block finishes executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/autoreleasefrequency/never)*