# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms whether you can perform the search.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func confirm(intent: INSearchForAccountsIntent, completion: @escaping @Sendable (INSearchForAccountsIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INSearchForAccountsIntent) async -> INSearchForAccountsIntentResponse
```

```objc
- (void) confirmSearchForAccounts:(INSearchForAccountsIntent *) intent completion:(void (^)(INSearchForAccountsIntentResponse *response)) completion;
```

#### Discussion

Implement this method to validate that you can perform the search using the given parameters, but do not perform the search yet. If the search involves contacting a remote server, you should also validate that the server is available. At some point in your implementation, execute the provided completion block with a response object indicating your app’s readiness to perform the search.

## Parameters

- `intent`: The intent object containing details about the user’s request. The information in this object has already been resolved by your handler object.
- `completion`: The handler block to execute with your response. You must execute this handler at some point during your implementation of this method. The handler has no return value and takes the following parameter:


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforaccountsintenthandling/confirm(intent:completion:))*