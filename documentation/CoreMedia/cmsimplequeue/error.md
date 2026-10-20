# CMSimpleQueue.Error

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A structure that defines errors that queue operations can produce.

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
struct Error
```

## Topics

### Errors
- [static let allocationFailed: NSError](./error/allocationfailed.md)
  The system failed to allocate memory.
- [static let queueIsFull: NSError](./error/queueisfull.md)
  An operation failed because the queue is full.
- [static let parameterOutOfRange: NSError](./error/parameteroutofrange.md)
  You passed a parameter to a function that’s outside the range of allowed values.
- [static let requiredParameterMissing: NSError](./error/requiredparametermissing.md)
  You failed to pass a required parameter to a function.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeue/error)*