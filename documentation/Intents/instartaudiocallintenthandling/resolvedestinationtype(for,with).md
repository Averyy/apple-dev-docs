# resolveDestinationType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the destination of the call.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 6.0

## Declaration

```swift
optional func resolveDestinationType(for intent: INStartAudioCallIntent, with completion: @escaping @Sendable (INCallDestinationTypeResolutionResult) -> Void)
```

```swift
optional func resolveDestinationType(for intent: INStartAudioCallIntent) async -> INCallDestinationTypeResolutionResult
```

```objc
- (void) resolveDestinationTypeForStartAudioCall:(INStartAudioCallIntent *) intent withCompletion:(void (^)(INCallDestinationTypeResolutionResult *resolutionResult)) completion;
```

#### Discussion

Use this method to verify that you can initiate the specified type of call. Return a successful resolution if you can place the specified type of call. If you don’t support the specified call type, return a not required or successful resolution and report the failure in your [`confirm(intent:completion:)`](./confirm%28intent,completion%29.md) method.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For a successful resolution, create a resolution result with the requested destination type.

## See Also

### Resolving the Intent Parameters
- [func resolveContacts(for: INStartAudioCallIntent, with: ([INPersonResolutionResult]) -> Void)](./resolvecontacts%28for,with%29.md)
  Resolves the recipients of the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartaudiocallintenthandling/resolvedestinationtype(for:with:))*