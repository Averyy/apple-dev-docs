# INIntentError.Code.deletingAllInteractions

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The system was unable to delete all donated INInteraction objects.

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
case deletingAllInteractions
```

```c
INIntentErrorDeletingAllInteractions
```

## Discussion

To determine the low-level cause of the problem, check the value of [`NSUnderlyingErrorKey`](../../../Foundation/nsunderlyingerrorkey.md) in the error object’s [`userInfo`](../../../Foundation/nserror/userinfo.md) dictionary.

## See Also

### Interaction Errors
- [INIntentError.Code.interactionOperationNotSupported](./interactionoperationnotsupported.md)
  The [`INInteraction`](../../ininteraction.md) object could not be donated or deleted because those capabilities are not supported on the current device.
- [INIntentError.Code.donatingInteraction](./donatinginteraction.md)
  The INInteraction object could not be donated to the system.
- [INIntentError.Code.deletingInteractionWithIdentifiers](./deletinginteractionwithidentifiers.md)
  The system was unable to delete the specified set of INInteraction objects.
- [INIntentError.Code.deletingInteractionWithGroupIdentifier](./deletinginteractionwithgroupidentifier.md)
  The system was unable to delete the INInteraction objects using their group identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintenterror/code/deletingallinteractions)*