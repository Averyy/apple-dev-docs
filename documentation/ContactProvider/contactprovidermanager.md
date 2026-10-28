# ContactProviderManager

**Framework**: ContactProvider  
**Kind**: class  
**Role**: Class

An interface for the app to control its extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
class ContactProviderManager
```

## Overview

Use this class to initially enable your contact provider app extension, making it visible to the system and other apps. To use the default domain, create a manager and call [`enable()`](./contactprovidermanager/enable%28%29.md). This is an `async` call, because it may prompt the person using your app to approve turning on the contact provider.

```swift
import ContactProvider

func enableExtensionExample() async {
    do {
        // The app creates a contact provider manager with a default domain.
        let manager = try ContactProviderManager()
        
        // May prompt the person to enable the default domain.
        try await manager.enable()
    } catch {
        // Handle the error.
    }
}
```

### Signaling the app extension

You also use `ContactProviderManager` when you need to invoke the app extension on demand. For example, when your app knows new contacts are available from your server, call [`signalEnumerator(for:)`](./contactprovidermanager/signalenumerator%28for%29.md) so the extension can fetch and provide the changed contacts.

```swift
import ContactProvider

func refreshForNewContacts() async {
    do {
        let manager = try ContactProviderManager()
        try await manager.signalEnumerator()
    } catch {
        // Handle the error.
    }
}
```

> ❗ **Important**: You can only use `ContactProviderManager` in an app, not in an app extension.

## Topics

### Creating a contact provider manager
- [init(domainIdentifier: String) throws](./contactprovidermanager/init%28domainidentifier%29.md)
  Creates a provider manager.
### Invoking the app extension
- [func signalEnumerator(for: ContactItem.Identifier) async throws](./contactprovidermanager/signalenumerator%28for%29.md)
  Requests that the extension enumerate its contacts for the domain.
### Managing the contact provider manager life cycle
- [func invalidate() async throws](./contactprovidermanager/invalidate%28%29.md)
  Requests that the extension terminate.
### Managing the domain
- [var domain: any ContactProviderDomain](./contactprovidermanager/domain.md)
  The domain that this instance manages.
- [func enable() async throws](./contactprovidermanager/enable%28%29.md)
  Requests the person using the app to enable the extension domain.
- [var isEnabled: Bool](./contactprovidermanager/isenabled.md)
  A Boolean value that indicates whether the person using the app enabled the extension domain.
- [func reset() async throws](./contactprovidermanager/reset%28%29.md)
  Resets the extension domain.
- [func disable() async throws](./contactprovidermanager/disable%28%29.md)
  Disables the extension domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactprovidermanager)*