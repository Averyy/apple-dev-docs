# ModelConfiguration.CloudKitDatabase

**Framework**: SwiftData  
**Kind**: struct

A type that describes the options for detecting a CloudKit database.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+
- Swift 5.9+

## Declaration

```swift
struct CloudKitDatabase
```

## Topics

### Getting discovery options
- [static var automatic: ModelConfiguration.CloudKitDatabase](modelconfiguration/cloudkitdatabase-swift.struct/automatic.md)
  Enables managed CloudKit sync using the primary ubiquity container from the app’s entitlements.
- [static func `private`(String) -> ModelConfiguration.CloudKitDatabase](modelconfiguration/cloudkitdatabase-swift.struct/private(_:).md)
  Enables managed CloudKit sync using the specified ubiquity container.
- [static var none: ModelConfiguration.CloudKitDatabase](modelconfiguration/cloudkitdatabase-swift.struct/none.md)
  Disables managed CloudKit sync.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let cloudKitContainerIdentifier: String?](modelconfiguration/cloudkitcontaineridentifier.md)
  The identifier of the configuration’s CloudKit database container.
- [let cloudKitDatabase: ModelConfiguration.CloudKitDatabase](modelconfiguration/cloudkitdatabase-swift.property.md)
  The option to use when detecting the container of the preferred CloudKit database.
- [let groupAppContainerIdentifier: String?](modelconfiguration/groupappcontaineridentifier.md)
  The identifier of the configuration’s app group container.
- [let groupContainer: ModelConfiguration.GroupContainer](modelconfiguration/groupcontainer-swift.property.md)
  The option to use when detecting the preferred app group container.
- [ModelConfiguration.GroupContainer](modelconfiguration/groupcontainer-swift.struct.md)
  A type that describes the options for detecting an app group container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/cloudkitdatabase-swift.struct)*