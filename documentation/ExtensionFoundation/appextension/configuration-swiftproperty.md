# configuration

**Framework**: ExtensionFoundation  
**Kind**: property  
**Required**: Yes

The configuration details for this app extension.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 9.0+

## Declaration

```swift
@MainActor
@preconcurrency var configuration: Self.Configuration { get }
```

#### Discussion

Implement this property in your custom type and use it to store the configuration details for your app extension. As part of the configuration, provide code to establish an XPC connection back to the host app.

If your app extension sends only data to the host app, and doesn’t provide a UI, use this property to store a type that implements the [`AppExtensionConfiguration`](appextensionconfiguration.md) protocol. If your extension provides UI elements for the host app to display, instead store an instance of the [`AppExtensionSceneConfiguration`](https://developer.apple.com/documentation/ExtensionKit/AppExtensionSceneConfiguration) type.

## See Also

- [associatedtype Configuration : AppExtensionConfiguration](appextension/configuration-swift.associatedtype.md)
  A type that manages configuration data for an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextension/configuration-swift.property)*