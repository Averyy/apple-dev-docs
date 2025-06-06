# presentationAnchor(for:)

**Framework**: Authentication Services  
**Kind**: method  
**Required**: Yes

Returns the most appropriate window for presenting the authentication modification interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentationAnchor(for controller: ASAccountAuthenticationModificationController) -> ASPresentationAnchor
```

#### Return Value

A window to present the authentication modification interface.

## Parameters

- `controller`: The controller that performs the account authentication modification request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontrollerpresentationcontextproviding/presentationanchor(for:))*