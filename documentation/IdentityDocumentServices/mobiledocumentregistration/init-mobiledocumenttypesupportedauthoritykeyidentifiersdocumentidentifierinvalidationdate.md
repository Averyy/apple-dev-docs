# init(mobileDocumentType:supportedAuthorityKeyIdentifiers:documentIdentifier:invalidationDate:)

**Framework**: IdentityDocumentServices  
**Kind**: init

Initializes a mobile document registration.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
init(mobileDocumentType: String, supportedAuthorityKeyIdentifiers: [Data], documentIdentifier: String = UUID().uuidString, invalidationDate: Date? = nil)
```

## Parameters

- `mobileDocumentType`: The type of the mobile document.
- `supportedAuthorityKeyIdentifiers`: A list of authority key identifiers that correspond to relying party authorizers that are trusted by the document provider app.
- `documentIdentifier`: An identifier that uniquely refers to the registered document. If not provided, the system chooses a random unique identifier.
- `invalidationDate`: A date that indicates when the system needs to invalidate this registration. You can use this date in scenarios where the expiration time period of a document is known.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/mobiledocumentregistration/init(mobiledocumenttype:supportedauthoritykeyidentifiers:documentidentifier:invalidationdate:))*