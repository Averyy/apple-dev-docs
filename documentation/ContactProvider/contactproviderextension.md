# ContactProviderExtension

**Framework**: ContactProvider  
**Kind**: protocol

The protocol your app extension implements, which provides contact items to the system-wide Contacts ecosystem.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
protocol ContactProviderExtension : ContactItemEnumerating, AppExtension
```

#### Overview

For the system to recognize your app extension, use the following identifier in the extension’s `Info.plist` file:

```swift
<key>EXAppExtensionAttributes</key>
<dict>
    <key>EXExtensionPointIdentifier</key>
    <string>com.apple.contact.provider.extension</string>
</dict>
```

Installing the host app installs your extension, but the system won’t run the extension until the extension domain is enabled. When the extension runs, the system first calls the extension’s [`configure(for:)`](contactproviderextension/configure(for:).md) method. Then you set up the enumerator that provides contact items from your data store.

The following shows a basic implementation of a `ContactProviderExtension`. Because `ContactProviderExtension` inherits from [`ContactItemEnumerating`](contactitemenumerating.md) the implementation also implements [`enumerator(for:)`](contactitemenumerating/enumerator(for:).md) which returns a [`ContactItemEnumerator`](contactitemenumerator.md) on demand. In this example, the extension sets up a `RootContainerEnumerator` to provide its contact items; see the [`ContactItemEnumerator`](contactitemenumerator.md) discussion for details of how `RootContainerEnumerator` works.

```swift
import ContactProvider

@main
class ExtensionExample: ContactProviderExtension {
    private let rootContainerEnumerator: RootContainerEnumerator
    
    required init() {
        rootContainerEnumerator = RootContainerEnumerator()
    }
    
    func configure(for domain: ContactProviderDomain) {
        rootContainerEnumerator.configure(for: domain)
    }
    
    func enumerator(for collection: ContactItem.Identifier) -> any ContactItemEnumerator {
        return rootContainerEnumerator
    }

    func invalidate() async {
        // Stop the enumeration and clean up, in preparation for the extension to terminate.
    }
}
```

## Topics

### Configuring an extension
- [func configure(for: any ContactProviderDomain)](contactproviderextension/configure(for:).md)
  Configures the extension instance for a domain.
### Managing the extension life cycle
- [func invalidate() async throws](contactproviderextension/invalidate.md)
  Invalidates the extension.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [ContactItemEnumerating](contactitemenumerating.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/contactprovider/contactproviderextension)*