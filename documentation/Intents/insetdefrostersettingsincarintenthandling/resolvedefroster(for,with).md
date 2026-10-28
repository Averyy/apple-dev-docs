# resolveDefroster(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves which defroster to change.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveDefroster(for intent: INSetDefrosterSettingsInCarIntent, with completion: @escaping @Sendable (INCarDefrosterResolutionResult) -> Void)
```

```swift
optional func resolveDefroster(for intent: INSetDefrosterSettingsInCarIntent) async -> INCarDefrosterResolutionResult
```

```objc
- (void) resolveDefrosterForSetDefrosterSettingsInCar:(INSetDefrosterSettingsInCarIntent *) intent withCompletion:(void (^)(INCarDefrosterResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the which defroster to use. Use the intent object to identify the defroster specified by the user. If the car has more than one climate zone, use the intent’s [`defroster`](../insetdefrostersettingsincarintent/defroster.md) property to identify the correct defroster.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object whose value contains the specified defroster. If the specified defroster isn’t available, create a resolution result that indicates the change isn’t supported.

## See Also

### Resolving the Intent Parameters
- [func resolveEnable(for: INSetDefrosterSettingsInCarIntent, with: (INBooleanResolutionResult) -> Void)](./resolveenable%28for,with%29.md)
  Resolves whether you can enable or disable the defroster setting.
- [func resolveCarName(for: INSetDefrosterSettingsInCarIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvecarname%28for,with%29.md)
  Resolves the car name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintenthandling/resolvedefroster(for:with:))*