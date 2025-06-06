# requestDocument(_:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Prompts the user to approve the request to get the identity information.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func requestDocument(_ request: PKIdentityRequest) async throws -> PKIdentityDocument
```

#### Discussion

The user needs to approve the request before releasing any data. When the user approves the request, the system returns the document. If the user doesn’t approve the request, the handler returns a [`PKIdentityError.Code.cancelled`](pkidentityerror-swift.struct/code/cancelled.md) error.

Only one request can be in progress at a time; otherwise, the method returns a [`PKIdentityError.Code.requestAlreadyInProgress`](pkidentityerror-swift.struct/code/requestalreadyinprogress.md) error.

Your app’s `Info.plist` file needs to provide a message for the `NSIdentityUsageDescription` key. If this key is missing, any attempt to request a document fails.

## Parameters

- `request`: The object that contains the identity elements the app requests.
- `completion`: The callback the system invokes after retrieving the document, or an error if one occurs.

## See Also

- [func checkCanRequestDocument(any PKIdentityDocumentDescriptor, completion: (Bool) -> Void)](pkidentityauthorizationcontroller/checkcanrequestdocument(_:completion:).md)
  Returns whether an identity document is available to request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentityauthorizationcontroller/requestdocument(_:completion:))*