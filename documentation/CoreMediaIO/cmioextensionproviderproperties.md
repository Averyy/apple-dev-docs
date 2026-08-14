# CMIOExtensionProviderProperties

**Framework**: Core Media I/O  
**Kind**: class

An object that manages the properties of an extension provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
class CMIOExtensionProviderProperties
```

#### Overview

Create an instance of this object to manage the provider’s property state.

## Topics

### Creating Provider Properties
- [init(dictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>])](cmioextensionproviderproperties/init(dictionary:).md)
  Creates a provider properties object with the specified properties.
### Managing Properties
- [var name: String?](cmioextensionproviderproperties/name.md)
  The provider name.
- [var manufacturer: String?](cmioextensionproviderproperties/manufacturer.md)
  The provider manufacturer.
- [func setPropertyState(CMIOExtensionPropertyState<AnyObject>?, forProperty: CMIOExtensionProperty)](cmioextensionproviderproperties/setpropertystate(_:forproperty:).md)
  Sets a state value for the specified property.
- [var propertiesDictionary: [CMIOExtensionProperty : CMIOExtensionPropertyState<AnyObject>]](cmioextensionproviderproperties/propertiesdictionary.md)
  A dictionary of properties for a provider.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Creating a camera extension with Core Media I/O](creating-a-camera-extension-with-core-media-i-o.md)
  Build high-performance camera drivers that are secure and simple to deploy.
- [Overriding the default USB video class extension](overriding-the-default-usb-video-class-extension.md)
  Create a simple DriverKit extension to override the default driver-matching behavior for USB devices.
- [class CMIOExtensionProvider](cmioextensionprovider.md)
  An object that manages device connections for a provider.
- [protocol CMIOExtensionProviderSource](cmioextensionprovidersource.md)
  A protocol for objects that act as provider sources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionproviderproperties)*