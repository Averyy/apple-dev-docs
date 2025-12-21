# ContactProviderError

**Framework**: ContactProvider  
**Kind**: enum

Errors thrown by the Contact Provider framework.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
enum ContactProviderError
```

## Topics

### Availability errors
- [ContactProviderError.featureNotAvailable](contactprovidererror/featurenotavailable.md)
  The extension can’t run because the feature isn’t available.
- [ContactProviderError.deniedByUser](contactprovidererror/deniedbyuser.md)
  The person using the app denied the action.
### Configuration errors
- [ContactProviderError.extensionNotFound](contactprovidererror/extensionnotfound.md)
  The framework couldn’t discover the app’s extension.
### Capacity errors
- [ContactProviderError.itemsLimitReached](contactprovidererror/itemslimitreached.md)
  Limit of items has been reached.
### Enumeration errors
- [ContactProviderError.cannotEnumerate](contactprovidererror/cannotenumerate.md)
  The extension is unable to enumerate.
- [ContactProviderError.enumerationTimeout](contactprovidererror/enumerationtimeout.md)
  The extension enumeration timed out.
### Expiration errors
- [ContactProviderError.pageExpired](contactprovidererror/pageexpired.md)
  The page expired and is no longer valid.
- [ContactProviderError.changeAnchorExpired](contactprovidererror/changeanchorexpired.md)
  The change anchor expired and is no longer valid.
### Invalidation errors
- [ContactProviderError.extensionInvalidated](contactprovidererror/extensioninvalidated.md)
  The app invalidated the extension while it was enumerating content or changes.
- [ContactProviderError.extensionInvalidateTimeout](contactprovidererror/extensioninvalidatetimeout.md)
  The extension invalidate operation timed out.
### Enumeration Cases
- [ContactProviderError.domainNotRegistered](contactprovidererror/domainnotregistered.md)
  The domain has not been registered.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidererror)*