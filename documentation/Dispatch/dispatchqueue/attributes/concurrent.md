# concurrent

**Framework**: Dispatch  
**Kind**: property

The queue schedules tasks concurrently.

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
static let concurrent: DispatchQueue.Attributes
```

#### Discussion

If this attribute is not present, the queue schedules tasks serially in first-in, first-out (FIFO) order.

## See Also

- [static let initiallyInactive: DispatchQueue.Attributes](dispatchqueue/attributes/initiallyinactive.md)
  The newly created queue is inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/attributes/concurrent)*