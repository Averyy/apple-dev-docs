# AppExtensionPoint.Bind

**Framework**: ExtensionFoundation  
**Kind**: struct

A property wrapper that binds an app extension to an extension point of a host app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
@resultBuilder
struct Bind
```

## Mentions

- [Building an app extension to support a host app](building-an-app-extension-to-support-a-host-app.md)

#### Overview

Apply this property wrapper to a variable that contains an [`AppExtensionPoint`](appextensionpoint.md) type. Use the variable to define the extension point that your app extension supports. An app extension can bind to only one extension point in a host app.

When configuring the [`AppExtensionPoint`](appextensionpoint.md) type for your variable, specify the host app and extension point details using an [`AppExtensionPoint.Identifier`](appextensionpoint/identifier.md) type. The following example shows how to create the variable in your app extension, specify the extension point you want, and create the binding:

```None
struct MyAppExtension: AppExtension {
    @AppExtensionPoint.Bind
    var extensionPoint: AppExtensionPoint {
        AppExtensionPoint.Identifier("com.example.hostapp”, name “HostAppFeature”)
    }
}
```

To ensure the system discovers your app extension’s bindings, add a user-defined build setting to your app extension target in Xcode. Set the build setting name to `EX_ENABLE_EXTENSION_POINT_GENERATION` and configure it with a value of `YES`. When this setting is present, the compiler places the necessary binding information in your app extension’s `Info.plist` file.

## Topics

### Annotating a binding
- [static func buildBlock(AppExtensionPoint.Identifier) -> AppExtensionPoint](appextensionpoint/bind/buildblock(_:).md)
  Passes an identifier to the extension point type.

## See Also

- [AppExtensionPoint.Identifier](appextensionpoint/identifier.md)
  The details of an extension point that your app extension supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/bind)*