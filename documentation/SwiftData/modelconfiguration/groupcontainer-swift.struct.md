# ModelConfiguration.GroupContainer

**Framework**: SwiftData  
**Kind**: struct  
**Role**: Structure

A type that describes the options for detecting an app group container.

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
struct GroupContainer
```

## Topics

### Getting discovery options
- [static var automatic: ModelConfiguration.GroupContainer](./groupcontainer-swift.struct/automatic.md)
  Tells SwiftData to use the app’s primary group container as the root location for the persistent storage.
- [static func identifier(String) -> ModelConfiguration.GroupContainer](./groupcontainer-swift.struct/identifier%28_%29.md)
  Tells SwiftData to use the specified group container as the root location for the app’s persistent storage.
- [static var none: ModelConfiguration.GroupContainer](./groupcontainer-swift.struct/none.md)
  Prevents SwiftData from using a group container as the root location for the app’s persistent storage.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sharing and syncing the model store
- [let cloudKitContainerIdentifier: String?](./cloudkitcontaineridentifier.md)
  The identifier of the configuration’s CloudKit database container.
- [let cloudKitDatabase: ModelConfiguration.CloudKitDatabase](./cloudkitdatabase-swift.property.md)
  The option to use when detecting the container of the preferred CloudKit database.
- [ModelConfiguration.CloudKitDatabase](./cloudkitdatabase-swift.struct.md)
  A type that describes the options for detecting a CloudKit database.
- [let groupAppContainerIdentifier: String?](./groupappcontaineridentifier.md)
  The identifier of the configuration’s app group container.
- [let groupContainer: ModelConfiguration.GroupContainer](./groupcontainer-swift.property.md)
  The option to use when detecting the preferred app group container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/modelconfiguration/groupcontainer-swift.struct)*