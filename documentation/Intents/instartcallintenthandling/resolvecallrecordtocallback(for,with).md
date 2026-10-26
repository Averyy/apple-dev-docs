# resolveCallRecordToCallBack(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the redial of a missed call.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
optional func resolveCallRecordToCallBack(for intent: INStartCallIntent, with completion: @escaping @Sendable (INCallRecordResolutionResult) -> Void)
```

```swift
optional func resolveCallRecordToCallBack(for intent: INStartCallIntent) async -> INCallRecordResolutionResult
```

```objc
- (void) resolveCallRecordToCallBackForStartCall:(INStartCallIntent *) intent withCompletion:(void (^)(INCallRecordResolutionResult *resolutionResult)) completion;
```

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

## See Also

### Resolving the Intent Parameters
- [func resolveCallCapability(for: INStartCallIntent, with: (INStartCallCallCapabilityResolutionResult) -> Void)](./resolvecallcapability%28for,with%29.md)
  Resolves the type of call to start.
- [func resolveContacts(for: INStartCallIntent, with: ([INStartCallContactResolutionResult]) -> Void)](./resolvecontacts%28for,with%29.md)
  Resolves the recipients of the call.
- [func resolveDestinationType(for: INStartCallIntent, with: (INCallDestinationTypeResolutionResult) -> Void)](./resolvedestinationtype%28for,with%29.md)
  Resolves the destination of the call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintenthandling/resolvecallrecordtocallback(for:with:))*