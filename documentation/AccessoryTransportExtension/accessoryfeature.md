# AccessoryFeature

**Framework**: Accessory Transport Extension  
**Kind**: protocol  
**Role**: Protocol

A protocol that identifies a kind of work that the framework carries between your accessory and your app.

**Availability**:
- iOS 26.5+

## Declaration

```swift
protocol AccessoryFeature : Sendable, AppExtensionPoint.Capability
```

## Overview

The framework defines a set of features using this protocol; don’t add conformances yourself.

Declare the features that your app supports in your app’s [`AccessoryDataProvider`](./accessorydataprovider.md) extension. The system routes each feature’s session data to the handler that you provide.

To send data in a format that your app defines, use [`AccessoryWorker`](./accessoryworker.md) or [`AccessoryGPUWorker`](./accessorygpuworker.md). For more information, see [Accessory features](./accessory-features.md).

## Topics

### Identifying the feature
- [static var featureID: String](./accessoryfeature/featureid.md)
  A string for the feature type.

## Relationships

### Inherits From
- [AppExtensionPoint.Capability](../ExtensionFoundation/appextensionpoint/capability.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [AccessoryGPUWorker](./accessorygpuworker.md)
- [AccessoryWorker](./accessoryworker.md)

## See Also

### Declaring features
- [protocol AccessoryDataProvider](./accessorydataprovider.md)
  A protocol for an extension that provides your accessory’s data for one or more of the framework’s features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeature)*