# AppExtensionPoint.Identifier

**Framework**: ExtensionFoundation  
**Kind**: struct

The details of an extension point that your app extension supports.

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
struct Identifier
```

## Mentions

- [Building an app extension to support a host app](building-an-app-extension-to-support-a-host-app.md)

#### Overview

When creating a binding in your app extension, use this type to specify the extension point details. When binding to a host app’s extension point, always initialize this type with the host app’s bundle identifier and extension point name.

## Topics

### Creating an identifier attribute
- [init(StaticString)](appextensionpoint/identifier/init(_:).md)
  Creates an identifier for binding to a system-defined extension point.
- [init(host: StaticString, name: StaticString)](appextensionpoint/identifier/init(host:name:).md)
  Creates an identifier for binding to a host app’s extension point.

## See Also

- [AppExtensionPoint.Bind](appextensionpoint/bind.md)
  A property wrapper that binds an app extension to an extension point of a host app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/identifier)*