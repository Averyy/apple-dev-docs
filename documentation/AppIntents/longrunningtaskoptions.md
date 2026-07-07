# LongRunningTaskOptions

**Framework**: App Intents  
**Kind**: struct

Options for configuring long-running tasks.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func performBackgroundTask<T>(options: LongRunningTaskOptions, operation: () async throws -> T) async throws -> T](longrunningintent/performbackgroundtask(options:operation:).md)
  Runs an operation in the background with an extended amount of time.
- [func performBackgroundTask<T>(options: LongRunningTaskOptions, operation: () async throws -> T, onCancel: (IntentCancellationReason) -> Void) async throws -> T](longrunningintent/performbackgroundtask(options:operation:oncancel:).md)
  Runs an operation in the background and provides a way to cancel the operation before it finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/longrunningtaskoptions)*