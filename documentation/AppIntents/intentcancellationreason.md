# IntentCancellationReason

**Framework**: App Intents  
**Kind**: struct

Reasons for the cancellation of an app intent’s operation.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
struct IntentCancellationReason
```

#### Overview

This type contains the possible reasons for the cancellation of an app intent. You don’t create instances of this type yourself. Instead, you receive a value in the cancellation handler you pass to the [`withIntentCancellationHandler(operation:onCancel:isolation:)`](cancellableintent/withintentcancellationhandler(operation:oncancel:isolation:).md) method when running your app intent’s code. Use the reason to make decisions about how to respond to the cancellation.

## Topics

### Type Properties
- [static var timeout: IntentCancellationReason](intentcancellationreason/timeout.md)
  An option that indicates the app intent exceeded the allowed time limit without reporting progress.
- [static var userCancelled: IntentCancellationReason](intentcancellationreason/usercancelled.md)
  An option that indicates someone explicitly canceled the intent.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func withIntentCancellationHandler<T>(operation: () async throws -> T, onCancel: (IntentCancellationReason) -> Void, isolation: isolated (any Actor)?) async rethrows -> T](cancellableintent/withintentcancellationhandler(operation:oncancel:isolation:).md)
  Runs an operation with a cancellation handler that receives a cancellation reason.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentcancellationreason)*