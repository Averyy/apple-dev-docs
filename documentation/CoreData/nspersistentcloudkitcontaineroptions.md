# NSPersistentCloudKitContainerOptions

**Framework**: Core Data  
**Kind**: class

An object that customizes how a store description aligns with a CloudKit database.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class NSPersistentCloudKitContainerOptions
```

## Mentions

- [Creating a Core Data Model for CloudKit](creating-a-core-data-model-for-cloudkit.md)
- [Setting Up Core Data with CloudKit](setting-up-core-data-with-cloudkit.md)

#### Overview

Use [`NSPersistentCloudKitContainerOptions`](nspersistentcloudkitcontaineroptions.md) to customize the behavior of an [`NSPersistentCloudKitContainer`](nspersistentcloudkitcontainer.md) or to create additional store descriptions that sync to other containers.

For more information about setting up multiple stores, see [`Setting Up Core Data with CloudKit`](setting-up-core-data-with-cloudkit.md).

## Topics

### Creating Container Options
- [init(containerIdentifier: String)](nspersistentcloudkitcontaineroptions/init(containeridentifier:).md)
  Initializes container options using the given CloudKit container identifier.
- [var containerIdentifier: String](nspersistentcloudkitcontaineroptions/containeridentifier.md)
  The identifier of the CloudKit container associated with a given store description.
- [var databaseScope: CKDatabase.Scope](nspersistentcloudkitcontaineroptions/databasescope-4c72t.md)
  The database scope — public, private, or shared — to use for a specified store in a persistent CloudKit container.

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

## See Also

- [Mirroring a Core Data store with CloudKit](mirroring-a-core-data-store-with-cloudkit.md)
  Back user interfaces with a local replica of a CloudKit private database.
- [Synchronizing a local store to the cloud](synchronizing-a-local-store-to-the-cloud.md)
  Share data between a user’s devices and other iCloud users.
- [class NSPersistentCloudKitContainer](nspersistentcloudkitcontainer.md)
  A container that encapsulates the Core Data stack in your app, and mirrors select persistent stores to a CloudKit private database.
- [Sharing Core Data objects between iCloud users](sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontaineroptions)*