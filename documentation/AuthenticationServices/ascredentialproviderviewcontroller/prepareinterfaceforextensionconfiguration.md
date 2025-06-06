# prepareInterfaceForExtensionConfiguration()

**Framework**: Authenticationservices  
**Kind**: method

Prepares the interface to enable the user to configure the extension.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepareInterfaceForExtensionConfiguration()
```

#### Discussion

The system calls this method after the user enables your extension in Settings. Use this method to prepare a user interface for configuring the extension. You can also use the method to tell the system what credential identities your extension supports by adding them to the shared [`ASCredentialIdentityStore`](ascredentialidentitystore.md) instance. Any identities you add become available as AutoFill suggestions.

After finishing configuration, tell the system to dismiss your view controller by calling the context’s [`completeExtensionConfigurationRequest()`](ascredentialproviderextensioncontext/completeextensionconfigurationrequest().md) method.

> **Note**:  To receive a call to this method, specify the [`ShowsConfigurationUI`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/ASCredentialProviderExtensionCapabilities/ShowsConfigurationUI) key with a value of `YES` in the [`ASCredentialProviderExtensionCapabilities`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes/ASCredentialProviderExtensionCapabilities) dictionary, within the [`NSExtensionAttributes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/NSExtensionAttributes) dictionary in the extension’s [`Information Property List`](https://developer.apple.com/documentation/BundleResources/Information-Property-List).

## See Also

- [class ASCredentialIdentityStore](ascredentialidentitystore.md)
  A container that your extension fills to provide credentials through the QuickType bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/prepareinterfaceforextensionconfiguration())*