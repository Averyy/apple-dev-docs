# LongRunningTaskOptions

**Framework**: App Intents  
**Kind**: struct

Options for configuring long-running tasks.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct LongRunningTaskOptions
```

#### Overview

When performing long-running tasks, specify these options to indicate additional resource requirements for the task. Pass these options to the [`performBackgroundTask(options:operation:)`](longrunningintent/performbackgroundtask(options:operation:).md) or [`performBackgroundTask(options:operation:onCancel:)`](longrunningintent/performbackgroundtask(options:operation:oncancel:).md) methods.

## Topics

### Type Properties
- [static let requiresGPU: LongRunningTaskOptions](longrunningtaskoptions/requiresgpu.md)
  An option that indicates the task requires GPU resources.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func performBackgroundTask<T>(options: LongRunningTaskOptions, operation: () async throws -> T) async throws -> T](longrunningintent/performbackgroundtask(options:operation:).md)
  Runs an operation in the background with an extended amount of time.
- [func performBackgroundTask<T>(options: LongRunningTaskOptions, operation: () async throws -> T, onCancel: (IntentCancellationReason) -> Void) async throws -> T](longrunningintent/performbackgroundtask(options:operation:oncancel:).md)
  Runs an operation in the background and provides a way to cancel the operation before it finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/longrunningtaskoptions)*