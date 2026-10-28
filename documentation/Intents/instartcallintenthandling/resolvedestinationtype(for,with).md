# resolveDestinationType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the destination of the call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func resolveDestinationType(for intent: INStartCallIntent, with completion: @escaping @Sendable (INCallDestinationTypeResolutionResult) -> Void)
```

```swift
optional func resolveDestinationType(for intent: INStartCallIntent) async -> INCallDestinationTypeResolutionResult
```

```objc
- (void) resolveDestinationTypeForStartCall:(INStartCallIntent *) intent withCompletion:(void (^)(INCallDestinationTypeResolutionResult *resolutionResult)) completion;
```

## Discussion

This method verifies that you can initiate the specified call type. Return a successful resolution if you can place the specified call type. If you don’t support the specified call type, return a not required resolution and report the failure in your [`confirm(intent:completion:)`](./confirm%28intent,completion%29.md) method.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For a successful resolution, create a resolution result with the requested destination type.

## See Also

### Resolving the Intent Parameters
- [func resolveCallCapability(for: INStartCallIntent, with: (INStartCallCallCapabilityResolutionResult) -> Void)](./resolvecallcapability%28for,with%29.md)
  Resolves the type of call to start.
- [func resolveContacts(for: INStartCallIntent, with: ([INStartCallContactResolutionResult]) -> Void)](./resolvecontacts%28for,with%29.md)
  Resolves the recipients of the call.
- [func resolveCallRecordToCallBack(for: INStartCallIntent, with: (INCallRecordResolutionResult) -> Void)](./resolvecallrecordtocallback%28for,with%29.md)
  Resolves the redial of a missed call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintenthandling/resolvedestinationtype(for:with:))*