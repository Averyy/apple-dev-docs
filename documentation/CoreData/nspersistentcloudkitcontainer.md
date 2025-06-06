# NSPersistentCloudKitContainer

**Framework**: Core Data  
**Kind**: class

A container that encapsulates the Core Data stack in your app, and mirrors select persistent stores to a CloudKit private database.

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
class NSPersistentCloudKitContainer
```

## Mentions

- [Setting Up Core Data with CloudKit](setting-up-core-data-with-cloudkit.md)
- [Mirroring a Core Data store with CloudKit](mirroring-a-core-data-store-with-cloudkit.md)
- [Reading CloudKit Records for Core Data](reading-cloudkit-records-for-core-data.md)

#### Overview

[`NSPersistentCloudKitContainer`](nspersistentcloudkitcontainer.md) is a subclass of [`NSPersistentContainer`](nspersistentcontainer.md) capable of managing both CloudKit-backed and noncloud stores.

By default, [`NSPersistentCloudKitContainer`](nspersistentcloudkitcontainer.md) contains a single store description, which Core Data assigns to the first CloudKit container identifier in an app’s entitlements. Use [`NSPersistentCloudKitContainerOptions`](nspersistentcloudkitcontaineroptions.md) to customize this behavior or create additional store descriptions with backing by different containers.

For more information about setting up multiple stores, see [`Setting Up Core Data with CloudKit`](setting-up-core-data-with-cloudkit.md).

## Topics

### Checking Permissions
- [func canUpdateRecord(forManagedObjectWith: NSManagedObjectID) -> Bool](nspersistentcloudkitcontainer/canupdaterecord(formanagedobjectwith:).md)
  Returns a Boolean value that indicates whether the user can modify the managed object’s underlying CloudKit record.
- [func canDeleteRecord(forManagedObjectWith: NSManagedObjectID) -> Bool](nspersistentcloudkitcontainer/candeleterecord(formanagedobjectwith:).md)
  Returns a Boolean value that indicates whether the user can delete the managed object’s underlying CloudKit record.
- [func canModifyManagedObjects(in: NSPersistentStore) -> Bool](nspersistentcloudkitcontainer/canmodifymanagedobjects(in:).md)
  Returns a Boolean value that indicates whether the user can modify the specified persistent store.
### Sharing Objects
- [Accepting Share Invitations in a SwiftUI App](accepting-share-invitations-in-a-swiftui-app.md)
  Adapt your app to use UIKit’s application and scene delegates so it can process CloudKit share invitations.
### Promoting Your Schema
- [func initializeCloudKitSchema(options: NSPersistentCloudKitContainerSchemaInitializationOptions) throws](nspersistentcloudkitcontainer/initializecloudkitschema(options:).md)
  Creates the CloudKit schema for all stores in the container that manage a CloudKit database.
- [struct NSPersistentCloudKitContainerSchemaInitializationOptions](nspersistentcloudkitcontainerschemainitializationoptions.md)
  Options that control the behavior when promoting the container’s schema to CloudKit.
### Monitoring Container Events
- [NSPersistentCloudKitContainer.Event](nspersistentcloudkitcontainer/event.md)
  An object that represents activity in a persistent CloudKit container.
- [NSPersistentCloudKitContainer.EventType](nspersistentcloudkitcontainer/eventtype.md)
  The type of event in a persistent CloudKit container, either setup, import, or export.
- [class NSPersistentCloudKitContainerEventRequest](nspersistentcloudkitcontainereventrequest.md)
  A request to fetch setup, import, or export events in a persistent CloudKit container.
- [class NSPersistentCloudKitContainerEventResult](nspersistentcloudkitcontainereventresult.md)
  The result of a request to fetch persistent CloudKit container events.
- [class let eventChangedNotification: NSNotification.Name](nspersistentcloudkitcontainer/eventchangednotification.md)
  A notification that contains details about an event in a persistent CloudKit container.
- [class let eventNotificationUserInfoKey: String](nspersistentcloudkitcontainer/eventnotificationuserinfokey.md)
  The user info dictionary key for the persistent CloudKit container event.

## Relationships

### Inherits From
- [NSPersistentContainer](nspersistentcontainer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Mirroring a Core Data store with CloudKit](mirroring-a-core-data-store-with-cloudkit.md)
  Back user interfaces with a local replica of a CloudKit private database.
- [Synchronizing a local store to the cloud](synchronizing-a-local-store-to-the-cloud.md)
  Share data between a user’s devices and other iCloud users.
- [class NSPersistentCloudKitContainerOptions](nspersistentcloudkitcontaineroptions.md)
  An object that customizes how a store description aligns with a CloudKit database.
- [Sharing Core Data objects between iCloud users](sharing-core-data-objects-between-icloud-users.md)
  Use Core Data and CloudKit to synchronize data between devices of an iCloud user and share data between different iCloud users.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontainer)*