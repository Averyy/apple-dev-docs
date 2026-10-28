# resolveContacts(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the recipients of the call.

**Availability**:
- iOS 10.0+ - Deprecated in 13.0
- iPadOS 10.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: INStartVideoCallIntent is deprecated. Please adopt INStartCallIntent instead

## Declaration

```swift
optional func resolveContacts(for intent: INStartVideoCallIntent, with completion: @escaping @Sendable ([INPersonResolutionResult]) -> Void)
```

```swift
optional func resolveContacts(for intent: INStartVideoCallIntent) async -> [INPersonResolutionResult]
```

```objc
- (void) resolveContactsForStartVideoCall:(INStartVideoCallIntent *) intent withCompletion:(void (^)(NSArray<INPersonResolutionResult *> *resolutionResults)) completion;
```

## Discussion

Use this method to verify the identity of any intended call recipients. Always strive toward a successful resolution to a specific user, but feel free to ask for confirmation of the selected user if there’s some uncertainty.

If you find multiple users matching the same name, consider asking the user to disambiguate from among the most likely candidates. When disambiguating users, provide as few choices as possible. If you find more than five possible users, consider a different resolution.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use the information in this object to resolve the list of contacts.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For each successful resolution, create a resolution result that includes the [`INPerson`](../inperson.md) object with the information that you need to call the user later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartvideocallintenthandling/resolvecontacts(for:with:))*