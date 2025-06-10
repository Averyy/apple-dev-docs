# Job

**Framework**: Swift  
**Kind**: struct

Deprecated equivalent of [`ExecutorJob`](executorjob.md).

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
@frozen
struct Job
```

#### Overview

A unit of schedulable work.

Unless you’re implementing a scheduler, you don’t generally interact with jobs directly.

## Topics

### Initializers
- [init(UnownedJob)](job/init(_:)-6f0eq.md)
- [init(ExecutorJob)](job/init(_:)-6pzn2.md)
### Instance Properties
- [var description: String](job/description.md)
- [var priority: JobPriority](job/priority.md)
### Instance Methods
- [func runSynchronously(on: UnownedSerialExecutor)](job/runsynchronously(on:).md)
  Run this job on the passed in executor.

## Relationships

### Conforms To
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/job)*