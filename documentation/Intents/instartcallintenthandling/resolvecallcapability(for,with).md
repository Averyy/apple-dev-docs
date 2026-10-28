# resolveCallCapability(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the type of call to start.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func resolveCallCapability(for intent: INStartCallIntent, with completion: @escaping @Sendable (INStartCallCallCapabilityResolutionResult) -> Void)
```

```swift
optional func resolveCallCapability(for intent: INStartCallIntent) async -> INStartCallCallCapabilityResolutionResult
```

```objc
- (void) resolveCallCapabilityForStartCall:(INStartCallIntent *) intent withCompletion:(void (^)(INStartCallCallCapabilityResolutionResult *resolutionResult)) completion;
```

## Discussion

This method lets SiriKit know which types of calls you can start. Your implementation should provide a successful resolution for the call types you support and an unsupported resolution for any call types you don’t support.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For a successful resolution, create a resolution result that contains the types of calls you are able to start.

## See Also

### Resolving the Intent Parameters
- [func resolveContacts(for: INStartCallIntent, with: ([INStartCallContactResolutionResult]) -> Void)](./resolvecontacts%28for,with%29.md)
  Resolves the recipients of the call.
- [func resolveDestinationType(for: INStartCallIntent, with: (INCallDestinationTypeResolutionResult) -> Void)](./resolvedestinationtype%28for,with%29.md)
  Resolves the destination of the call.
- [func resolveCallRecordToCallBack(for: INStartCallIntent, with: (INCallRecordResolutionResult) -> Void)](./resolvecallrecordtocallback%28for,with%29.md)
  Resolves the redial of a missed call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintenthandling/resolvecallcapability(for:with:))*