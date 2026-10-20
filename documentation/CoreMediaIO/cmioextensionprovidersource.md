# CMIOExtensionProviderSource

**Framework**: Core Media I/O  
**Kind**: protocol  
**Role**: Protocol

A protocol for objects that act as provider sources.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
protocol CMIOExtensionProviderSource : NSObjectProtocol
```

```objc
@protocol CMIOExtensionProviderSource <NSObject>
```

#### Overview

Create a class that adopts this protocol to configure provider properties and manage its client connections.

## Topics

### Managing Connections
- [func connect(to: CMIOExtensionClient) throws](./cmioextensionprovidersource/connect%28to%29.md)
  Connects a client to a source’s provider.
- [func disconnect(from: CMIOExtensionClient)](./cmioextensionprovidersource/disconnect%28from%29.md)
  Disconnects a client from a source’s provider.
### Configuring Properties
- [var availableProperties: Set<CMIOExtensionProperty>](./cmioextensionprovidersource/availableproperties.md)
  A set of available properties for a provider.
- [func providerProperties(forProperties: Set<CMIOExtensionProperty>) throws -> CMIOExtensionProviderProperties](./cmioextensionprovidersource/providerproperties%28forproperties%29.md)
  Gets the state of provider properties.
- [func setProviderProperties(CMIOExtensionProviderProperties) throws](./cmioextensionprovidersource/setproviderproperties%28_%29.md)
  Set the state of provider properties.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Providers
- [Creating a camera extension with Core Media I/O](./creating-a-camera-extension-with-core-media-i-o.md)
  Build high-performance camera drivers that are secure and simple to deploy.
- [Overriding the default USB video class extension](./overriding-the-default-usb-video-class-extension.md)
  Create a simple DriverKit extension to override the default driver-matching behavior for USB devices.
- [class CMIOExtensionProvider](./cmioextensionprovider.md)
  An object that manages device connections for a provider.
- [class CMIOExtensionProviderProperties](./cmioextensionproviderproperties.md)
  An object that manages the properties of an extension provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovidersource)*