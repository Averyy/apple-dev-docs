# init(domainIdentifier:)

**Framework**: ContactProvider  
**Kind**: init  
**Role**: Initializer

Creates a provider manager.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
init(domainIdentifier: String = DefaultContactProviderDomain.identifier) throws
```

## Discussion

If needed, the manager registers the [`DefaultContactProviderDomain`](../defaultcontactproviderdomain.md) for the extension.

> **Throws**: [`ContactProviderError.extensionNotFound`](../contactprovidererror/extensionnotfound.md) if discovering the extension fails.

> **Throws**: [`ContactProviderError.featureNotAvailable`](../contactprovidererror/featurenotavailable.md) when running on an unsupported platform.

## Parameters

- `domainIdentifier`: A string to identify a domain of contacts to provide. Defaults to [`identifier`](../defaultcontactproviderdomain/identifier.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager/init(domainidentifier:))*