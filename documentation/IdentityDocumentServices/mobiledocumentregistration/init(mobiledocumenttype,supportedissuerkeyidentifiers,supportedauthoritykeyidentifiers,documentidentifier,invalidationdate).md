# init(mobileDocumentType:supportedIssuerKeyIdentifiers:supportedAuthorityKeyIdentifiers:documentIdentifier:invalidationDate:)

**Framework**: IdentityDocumentServices  
**Kind**: init  
**Role**: Initializer

Initializes a mobile document registration with issuer key identifiers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst

## Declaration

```swift
init(mobileDocumentType: String, supportedIssuerKeyIdentifiers: [Data], supportedAuthorityKeyIdentifiers: [Data], documentIdentifier: String = UUID().uuidString, invalidationDate: Date? = nil)
```

## Parameters

- `mobileDocumentType`: The type of the mobile document.
- `supportedIssuerKeyIdentifiers`: A list of X.509 authority key identifiers that correspond to the document signer certificate chain for the mobile document.
- `supportedAuthorityKeyIdentifiers`: A list of authority key identifiers that correspond to relying party authorizers that are trusted by the document provider app.
- `documentIdentifier`: An identifier that uniquely refers to a registered document. If you don’t provide this identifier, the system chooses a random unique identifier.
- `invalidationDate`: A date that indicates when a registration becomes invalid. Use this parameter in scenarios where the expiration time period of a document is known.


---

*[View on Apple Developer](https://developer.apple.com/documentation/identitydocumentservices/mobiledocumentregistration/init(mobiledocumenttype:supportedissuerkeyidentifiers:supportedauthoritykeyidentifiers:documentidentifier:invalidationdate:))*