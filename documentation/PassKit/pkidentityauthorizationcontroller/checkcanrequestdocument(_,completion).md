# checkCanRequestDocument(_:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Returns whether an identity document is available to request.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func checkCanRequestDocument(_ descriptor: any PKIdentityDocumentDescriptor, completion: @escaping @Sendable (Bool) -> Void)
```

```swift
func canRequestDocument(_ descriptor: any PKIdentityDocumentDescriptor) async -> Bool
```

```objc
- (void) checkCanRequestDocument:(id<PKIdentityDocumentDescriptor>) descriptor completion:(void (^)(BOOL canRequest)) completion;
```

## Mentions

- [Requesting identity data from a Wallet pass](../requesting-identity-data-from-a-wallet-pass.md)

## Discussion

This method checks whether you have the correct entitlements and if the device has an ID in the Wallet app.

```swift
// Check whether the app can request the document.
controller.checkCanRequestDocument(descriptor) { canRequest in
    if canRequest {
        // Show the identity button for triggering the request.
    } else {
        // Hide the request button.
    }
}
```

## Parameters

- `descriptor`: The object that describes the document the app requests.
- `completion`: The callback the system invokes after determining whether you can request the document you describe.

## See Also

### Requesting a document
- [func requestDocument(PKIdentityRequest, completion: (PKIdentityDocument?, (any Error)?) -> Void)](./requestdocument%28_,completion%29.md)
  Prompts the user to approve the request to get the identity information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityauthorizationcontroller/checkcanrequestdocument(_:completion:))*