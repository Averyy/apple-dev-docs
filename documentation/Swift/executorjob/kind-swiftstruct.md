# ExecutorJob.Kind

**Framework**: Swift  
**Kind**: struct

Kinds of schedulable jobs

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@frozen
struct Kind
```

## Topics

### Initializers
- [init?(rawValue: ExecutorJob.Kind.RawValue)](executorjob/kind-swift.struct/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: ExecutorJob.Kind.RawValue](executorjob/kind-swift.struct/rawvalue-swift.property.md)
  The raw job kind value.
### Type Aliases
- [ExecutorJob.Kind.RawValue](executorjob/kind-swift.struct/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let firstReserved: ExecutorJob.Kind](executorjob/kind-swift.struct/firstreserved.md)
- [static let task: ExecutorJob.Kind](executorjob/kind-swift.struct/task.md)
  A task.

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [RawRepresentable](rawrepresentable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/executorjob/kind-swift.struct)*