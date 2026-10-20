# CKOperation.Configuration

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that describes how a CloudKit operation behaves.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class Configuration
```

```objc
@interface CKOperationConfiguration : NSObject
```

#### Overview

All of the properties in `CKOperationConfiguration` have a default value. When determining which properties to apply to a CloudKit operation, consult the operation’s configuration property, as well as the [`defaultConfiguration`](../ckoperationgroup/defaultconfiguration.md) property of the group that the operation belongs to. These properties combine through the following rules:

| Group default configuration value | Operation configuration value | Value applied to operation |
| --- | --- | --- |
| default value | default value | default value |
| default value | explicit value | operation.configuration explicit value |
| explicit value | default value | group.defaultConfiguration explicit value |
| explicit value | explicit value | operation.configuration explicit value |

## Topics

### Preparing a Configuration
- [var allowsCellularAccess: Bool](./configuration-swift.class/allowscellularaccess.md)
  A Boolean value that indicates whether operations that use this configuration can send data over the cellular network.
- [var container: CKContainer?](./configuration-swift.class/container.md)
  The configuration’s container.
- [var isLongLived: Bool](./configuration-swift.class/islonglived.md)
  A Boolean value that indicates whether the operations that use this configuration are long-lived.
- [var qualityOfService: QualityOfService](./configuration-swift.class/qualityofservice.md)
  The priority that the system uses when it allocates resources to the operations that use this configuration.
- [var timeoutIntervalForRequest: TimeInterval](./configuration-swift.class/timeoutintervalforrequest.md)
  The maximum amount of time that a request can take.
- [var timeoutIntervalForResource: TimeInterval](./configuration-swift.class/timeoutintervalforresource.md)
  The maximum amount of time that a resource request can take.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the Operation’s Configuration
- [var configuration: CKOperation.Configuration!](./configuration-swift.property.md)
  The operation’s configuration.
- [var group: CKOperationGroup?](./group.md)
  The operation’s group.
- [var longLivedOperationWasPersistedBlock: (() -> Void)?](./longlivedoperationwaspersistedblock.md)
  The closure to execute when the server begins to store callbacks for the long-lived operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/configuration-swift.class)*