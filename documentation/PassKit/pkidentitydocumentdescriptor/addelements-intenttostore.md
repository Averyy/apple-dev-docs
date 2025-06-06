# addElements(_:intentToStore:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Required**: Yes

Adds a list of identity element and defines the way an app, or it’s server, stores the elements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func addElements(_ elements: [PKIdentityElement], intentToStore: PKIdentityIntentToStore)
```

## Parameters

- `elements`: A list of identity elements.
- `intentToStore`: An object that defines how long an app or it’s server stores the elements.

## See Also

- [class PKIdentityIntentToStore](pkidentityintenttostore.md)
  An object that represents your intention to store an identity element or values derived from an identity element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydocumentdescriptor/addelements(_:intenttostore:))*