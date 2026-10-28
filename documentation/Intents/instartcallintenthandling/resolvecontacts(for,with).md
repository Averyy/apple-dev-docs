# resolveContacts(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the recipients of the call.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
optional func resolveContacts(for intent: INStartCallIntent, with completion: @escaping @Sendable ([INStartCallContactResolutionResult]) -> Void)
```

```swift
optional func resolveContacts(for intent: INStartCallIntent) async -> [INStartCallContactResolutionResult]
```

```objc
- (void) resolveContactsForStartCall:(INStartCallIntent *) intent withCompletion:(void (^)(NSArray<INStartCallContactResolutionResult *> *resolutionResults)) completion;
```

## Discussion

This method verifies the identity of any intended call recipients. Always strive toward a successful resolution to a specific user, but feel free to ask the user for confirmation of the selected contact if there’s some uncertainty.

If you find multiple users matching the same name, consider asking the user to disambiguate from among the most likely candidates. When disambiguating users, provide only a few choices. If you find more than five possible users, consider a different resolution.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For a successful resolution, create a resolution result that includes the [`INPerson`](../inperson.md) object with the information that you need to call the user later.

## See Also

### Resolving the Intent Parameters
- [func resolveCallCapability(for: INStartCallIntent, with: (INStartCallCallCapabilityResolutionResult) -> Void)](./resolvecallcapability%28for,with%29.md)
  Resolves the type of call to start.
- [func resolveDestinationType(for: INStartCallIntent, with: (INCallDestinationTypeResolutionResult) -> Void)](./resolvedestinationtype%28for,with%29.md)
  Resolves the destination of the call.
- [func resolveCallRecordToCallBack(for: INStartCallIntent, with: (INCallRecordResolutionResult) -> Void)](./resolvecallrecordtocallback%28for,with%29.md)
  Resolves the redial of a missed call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartcallintenthandling/resolvecontacts(for:with:))*