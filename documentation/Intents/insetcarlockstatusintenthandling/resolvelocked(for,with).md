# resolveLocked(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the requested lock status (locked or unlocked).

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveLocked(for intent: INSetCarLockStatusIntent, with completion: @escaping @Sendable (INBooleanResolutionResult) -> Void)
```

```swift
optional func resolveLocked(for intent: INSetCarLockStatusIntent) async -> INBooleanResolutionResult
```

```objc
- (void) resolveLockedForSetCarLockStatus:(INSetCarLockStatusIntent *) intent withCompletion:(void (^)(INBooleanResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to verify the requested lock status. This status is a Boolean value: [`true`](../../Swift/true.md) indicates that the car should be locked, [`false`](../../Swift/false.md) indicates it should be unlocked.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the requested lock status (locked or unlocked).

## See Also

### Resolving the Intent Parameters
- [func resolveCarName(for: INSetCarLockStatusIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvecarname%28for,with%29.md)
  Resolves the name of the user’s car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintenthandling/resolvelocked(for:with:))*