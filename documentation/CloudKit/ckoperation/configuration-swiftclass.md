# CKOperation.Configuration

**Framework**: CloudKit  
**Kind**: class

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

#### Overview

All of the properties in `CKOperationConfiguration` have a default value. When determining which properties to apply to a CloudKit operation, consult the operation’s configuration property, as well as the [`defaultConfiguration`](ckoperationgroup/defaultconfiguration.md) property of the group that the operation belongs to. These properties combine through the following rules:

| Group default configuration value | Operation configuration value | Value applied to operation |
| --- | --- | --- |
| default value | default value | default value |
| default value | explicit value | operation.configuration explicit value |
| explicit value | default value | group.defaultConfiguration explicit value |
| explicit value | explicit value | operation.configuration explicit value |

## Topics

### Preparing a Configuration
- [var allowsCellularAccess: Bool](ckoperation/configuration-swift.class/allowscellularaccess.md)
  A Boolean value that indicates whether operations that use this configuration can send data over the cellular network.
- [var container: CKContainer?](ckoperation/configuration-swift.class/container.md)
  The configuration’s container.
- [var isLongLived: Bool](ckoperation/configuration-swift.class/islonglived.md)
  A Boolean value that indicates whether the operations that use this configuration are long-lived.
- [var qualityOfService: QualityOfService](ckoperation/configuration-swift.class/qualityofservice.md)
  The priority that the system uses when it allocates resources to the operations that use this configuration.
- [var timeoutIntervalForRequest: TimeInterval](ckoperation/configuration-swift.class/timeoutintervalforrequest.md)
  The maximum amount of time that a request can take.
- [var timeoutIntervalForResource: TimeInterval](ckoperation/configuration-swift.class/timeoutintervalforresource.md)
  The maximum amount of time that a resource request can take.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var configuration: CKOperation.Configuration!](ckoperation/configuration-swift.property.md)
  The operation’s configuration.
- [var group: CKOperationGroup?](ckoperation/group.md)
  The operation’s group.
- [var longLivedOperationWasPersistedBlock: (() -> Void)?](ckoperation/longlivedoperationwaspersistedblock.md)
  The closure to execute when the server begins to store callbacks for the long-lived operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckoperation/configuration-swift.class)*