# interactionOperationNotSupported

**Framework**: Intents  
**Kind**: property  
**Role**: Type Property

The [`INInteraction`](../ininteraction.md) object could not be donated or deleted because those capabilities are not supported on the current device.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
static var interactionOperationNotSupported: INIntentError.Code { get }
```

## See Also

### Interaction Errors
- [static var donatingInteraction: INIntentError.Code](./donatinginteraction.md)
  The [`INInteraction`](../ininteraction.md) object could not be donated to the system.
- [static var deletingAllInteractions: INIntentError.Code](./deletingallinteractions.md)
  The system was unable to delete all donated [`INInteraction`](../ininteraction.md) objects.
- [static var deletingInteractionWithIdentifiers: INIntentError.Code](./deletinginteractionwithidentifiers.md)
  The system was unable to delete the specified set of [`INInteraction`](../ininteraction.md) objects.
- [static var deletingInteractionWithGroupIdentifier: INIntentError.Code](./deletinginteractionwithgroupidentifier.md)
  The system was unable to delete the [`INInteraction`](../ininteraction.md) objects using their group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintenterror/interactionoperationnotsupported)*