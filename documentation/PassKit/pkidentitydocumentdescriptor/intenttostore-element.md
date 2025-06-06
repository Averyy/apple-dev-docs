# intentToStore(element:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Required**: Yes

Gets the intent to store for an identity element you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func intentToStore(element: PKIdentityElement) -> PKIdentityIntentToStore?
```

#### Return Value

A [`PKIdentityIntentToStore`](pkidentityintenttostore.md) for the element, if available.

## Parameters

- `element`: The element to inspect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydocumentdescriptor/intenttostore(element:))*