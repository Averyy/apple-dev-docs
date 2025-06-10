# NSPersistentContainer

**Framework**: Core Data  
**Kind**: class

A container that encapsulates the Core Data stack in your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class NSPersistentContainer
```

## Mentions

- [Setting Up Core Data with CloudKit](setting-up-core-data-with-cloudkit.md)
- [Setting up a Core Data stack manually](setting-up-a-core-data-stack-manually.md)
- [Using Core Data in the background](using-core-data-in-the-background.md)
- [Setting up a Core Data stack](setting-up-a-core-data-stack.md)

#### Overview

NSPersistentContainer simplifies the creation and management of the Core Data stack by handling the creation of the managed object model ([`NSManagedObjectModel`](nsmanagedobjectmodel.md)), persistent store coordinator ([`NSPersistentStoreCoordinator`](nspersistentstorecoordinator.md)), and the managed object context ([`NSManagedObjectContext`](nsmanagedobjectcontext.md)).

## Topics

### Creating a Container
- [convenience init(name: String)](nspersistentcontainer/init(name:).md)
  Creates a container with the specified name.
- [init(name: String, managedObjectModel: NSManagedObjectModel)](nspersistentcontainer/init(name:managedobjectmodel:).md)
  Create a container with the specified name and managed object model.
### Getting the Container’s Configuration
- [var managedObjectModel: NSManagedObjectModel](nspersistentcontainer/managedobjectmodel.md)
  The container’s managed object model.
- [var name: String](nspersistentcontainer/name.md)
  The container’s name.
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator](nspersistentcontainer/persistentstorecoordinator.md)
  The container’s persistent store coordinator.
### Accessing the Default Directory
- [class var defaultDirectoryURL: URL](nspersistentcontainer/defaultdirectoryurl-swift.type.property.md)
  The location of the directory that contains the persistent stores.
- [class func defaultDirectoryURL() -> URL](nspersistentcontainer/defaultdirectoryurl.md)
  Returns the location of the directory that contains the persistent stores.
### Managing Persistent Stores
- [var persistentStoreDescriptions: [NSPersistentStoreDescription]](nspersistentcontainer/persistentstoredescriptions.md)
  The descriptions of the container’s persistent stores.
- [func loadPersistentStores(completionHandler: (NSPersistentStoreDescription, (any Error)?) -> Void)](nspersistentcontainer/loadpersistentstores(completionhandler:).md)
  Loads the persistent stores.
### Acquiring Contexts
- [func newBackgroundContext() -> NSManagedObjectContext](nspersistentcontainer/newbackgroundcontext.md)
  Returns a new managed object context that executes on a private queue.
- [var viewContext: NSManagedObjectContext](nspersistentcontainer/viewcontext.md)
  The main queue’s managed object context.
### Performing Background Tasks
- [func performBackgroundTask((NSManagedObjectContext) -> Void)](nspersistentcontainer/performbackgroundtask(_:)-39sch.md)
  Executes a closure on a private queue using an ephemeral managed object context.
- [func performBackgroundTask<T>((NSManagedObjectContext) throws -> T) async rethrows -> T](nspersistentcontainer/performbackgroundtask(_:)-25nok.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSPersistentCloudKitContainer](nspersistentcloudkitcontainer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcontainer)*