# initiallyInactive

**Framework**: Dispatch  
**Kind**: property

The newly created queue is inactive.

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
static let initiallyInactive: DispatchQueue.Attributes
```

#### Discussion

Normally, a newly created queue schedules submitted blocks for execution immediately. Use this attribute to prevent the queue from scheduling blocks until you call its [`activate()`](dispatchobject/activate().md) method.

## See Also

- [static let concurrent: DispatchQueue.Attributes](dispatchqueue/attributes/concurrent.md)
  The queue schedules tasks concurrently.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchqueue/attributes/initiallyinactive)*