# AppExtensionPoint

**Framework**: ExtensionFoundation  
**Kind**: struct

A type you use to declare your host app’s extension points and bind to them from app extensions.

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
struct AppExtensionPoint
```

## Mentions

- [Adding support for app extensions to your app](adding-support-for-app-extensions-to-your-app.md)
- [Building an app extension to support a host app](building-an-app-extension-to-support-a-host-app.md)

#### Overview

Use this type both to declare your app’s supported extension points and to bind to those extension points. To declare an extension point your app supports, extend this type by adding a static variable with the details of your extension point. Annotate your variable with the [`AppExtensionPoint.Definition`](appextensionpoint/definition.md) property wrapper and specify the name and other attributes of your extension point. The following example adds two extension point with different configurations:

```None
extension AppExtensionPoint {
    @Definition
    static var MySecureFeature : AppExtensionPoint {
        Name(“MySecureFeature”)
        UserInterface(false)
        EnhancedSecurity(true)
    }

    @Definition
    static var MyInterfaceFeature : AppExtensionPoint {
        Name(“MyInterfaceFeature”)
        UserInterface(true)
    }

}
```

In addition to defining your app’s extension points, use this type in an app extension to bind to an extension point. In your app extension’s source code, add a variable that contains the `AppExtensionPoint` type. Set the value of that variable to the extension point identifier you support. Annotate your variable declaration with the [`AppExtensionPoint.Bind`](appextensionpoint/bind.md) property wrapper, as shown in the following example:

```None
struct MyAppExtension: AppExtension {
    @AppExtensionPoint.Bind
    var boundAppExtensionPoint: AppExtensionPoint {
        AppExtensionPoint.Identifier(name “MySecureFeature”)
    }
}
```

To make extension point and binding information available at runtime, use the compiler to add the relevant information to your built products. In your Xcode project, add the `EX_ENABLE_EXTENSION_POINT_GENERATION` flag to the build settings of your host app and app extension. When the value of the flag is `true`, the compiler collects the target’s extension point definitions or bindings and writes them to the target’s bundle. For example, it creates a special file in the host app’s bundle and adds the extension point definitions to that file. The system collects definition and binding information at installation time and uses it to match the host app to relevant app extensions.

## Topics

### Creating an app-extension point
- [init(identifier: StaticString) throws](appextensionpoint/init(identifier:).md)
  Initializes the type with a string you can use to find the extension point.
### Declaring an extension point
- [AppExtensionPoint.Definition](appextensionpoint/definition.md)
  A property wrapper that a host app uses to declare the extension points it supports.
- [AppExtensionPoint.Name](appextensionpoint/name.md)
  A type that defines the name of an extension point.
- [AppExtensionPoint.UserInterface](appextensionpoint/userinterface.md)
  A type with that indicates whether the extension point displays UI from an app extension.
- [AppExtensionPoint.EnhancedSecurity](appextensionpoint/enhancedsecurity.md)
  A type that indicates whether an extension point requires extra security.
- [AppExtensionPoint.Scope](appextensionpoint/scope.md)
  A type that regulates which app extensions may access an extension point.
- [AppExtensionPoint.Attribute](appextensionpoint/attribute.md)
  An interface that marks a type as an extension point attribute.
### Binding to an extension point
- [AppExtensionPoint.Bind](appextensionpoint/bind.md)
  A property wrapper that binds an app extension to an extension point of a host app.
- [AppExtensionPoint.Identifier](appextensionpoint/identifier.md)
  The details of an extension point that your app extension supports.
### Detecting app extensions
- [AppExtensionPoint.Monitor](appextensionpoint/monitor.md)
  A type you use to discover the app extensions available for your host app to use.
### Getting error codes
- [AppExtensionPoint.Error](appextensionpoint/error.md)
  Error codes for monitor-related requests.
### Protocols
- [AppExtensionPoint.Capability](appextensionpoint/capability.md)
  An interface that marks a type as an extension capability.
### Structures
- [AppExtensionPoint.Capabilities](appextensionpoint/capabilities.md)
  The capabilities that an your extension implements

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExtensionPointDefining](extensionpointdefining.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol ExtensionPointDefining](extensionpointdefining.md)
  An interface that extension point types adopt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint)*