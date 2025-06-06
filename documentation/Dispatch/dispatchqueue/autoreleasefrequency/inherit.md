# DispatchQueue.AutoreleaseFrequency.inherit

**Framework**: Dispatch  
**Kind**: case

The queue inherits its autorelease frequency from its target queue.

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
case inherit
```

#### Discussion

This option is the default behavior for queues you create.

## See Also

- [DispatchQueue.AutoreleaseFrequency.workItem](dispatchqueue/autoreleasefrequency/workitem.md)
  The queue configures an autorelease pool before the execution of a block, and releases the objects in that pool after the block finishes executing.
- [DispatchQueue.AutoreleaseFrequency.never](dispatchqueue/autoreleasefrequency/never.md)
  The queue does not set up an autorelease pool around executed blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/autoreleasefrequency/inherit)*