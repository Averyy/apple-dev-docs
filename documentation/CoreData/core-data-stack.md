# Core Data stack

**Framework**: Core Data

Manage and persist your app’s model layer.

#### Overview

Core Data provides a set of classes that collaboratively support your app’s model layer:

- An instance of [`NSManagedObjectModel`](nsmanagedobjectmodel.md) describes your app’s types, including their properties and relationships.
- An instance of [`NSManagedObjectContext`](nsmanagedobjectcontext.md) tracks changes to instances of your app’s types.
- An instance of [`NSPersistentStoreCoordinator`](nspersistentstorecoordinator.md) saves and fetches instances of your app’s types from stores.

![Diagram showing that a persistent container instance contains references to a managed object model, a managed object context, and a persistent store coordinator that connects to your app’s stores.](https://docs-assets.developer.apple.com/published/5d911adb8af302c1be92e9a1ceb1bef7/media-3118356%402x.png)

You use an [`NSPersistentContainer`](nspersistentcontainer.md) instance to set up the model, context, and store coordinator simultaneously.

## Topics

### Stack Setup
- [class NSPersistentContainer](nspersistentcontainer.md)
  A container that encapsulates the Core Data stack in your app.
### Object Modeling
- [class NSManagedObjectModel](nsmanagedobjectmodel.md)
  A programmatic representation of the `.xcdatamodeld` file describing your objects.
- [class NSEntityDescription](nsentitydescription.md)
  A description of a Core Data entity.
- [class NSPropertyDescription](nspropertydescription.md)
  A description of a single property belonging to an entity.
- [class NSAttributeDescription](nsattributedescription.md)
  A description of a single attribute belonging to an entity.
- [class NSDerivedAttributeDescription](nsderivedattributedescription.md)
  A description of an attribute that derives its value by performing a calculation on a related attribute.
- [class NSRelationshipDescription](nsrelationshipdescription.md)
  A description of a relationship between two entities.
### Object Management
- [class NSManagedObjectContext](nsmanagedobjectcontext.md)
  An object space to manipulate and track changes to managed objects.
- [class NSManagedObject](nsmanagedobject.md)
  The base class that all Core Data model objects inherit from.
- [class NSManagedObjectID](nsmanagedobjectid.md)
  A compact, universal identifier for a managed object.
### Store Coordination
- [class NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)
  An object that enables an app’s contexts and the underlying persistent stores to work together.
- [class NSPersistentStore](nspersistentstore.md)
  The abstract base class for all Core Data persistent stores.
- [class NSPersistentStoreDescription](nspersistentstoredescription.md)
  A description object used to create and load a persistent store.
- [class NSPersistentStoreRequest](nspersistentstorerequest.md)
  Criteria used to retrieve data from or save data to a persistent store.
- [class NSPersistentStoreResult](nspersistentstoreresult.md)
  The abstract base class for results returned from a persistent store coordinator.
- [class NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md)
  A concrete class used to represent the results of an asynchronous request.
- [class NSSaveChangesRequest](nssavechangesrequest.md)
  An encapsulation of a collection of changes to be made by an object store in response to a save operation on a managed object context.
- [class NSAtomicStore](nsatomicstore.md)
  An abstract superclass that you subclass to create a Core Data atomic store.
- [class NSAtomicStoreCacheNode](nsatomicstorecachenode.md)
  A concrete class that you use to represent basic nodes in a Core Data atomic store.
- [class NSIncrementalStore](nsincrementalstore.md)
  An abstract superclass defining the API through which Core Data communicates with a store.
- [class NSIncrementalStoreNode](nsincrementalstorenode.md)
  A concrete class used to represent basic nodes in a Core Data incremental store.

## See Also

- [Creating a Core Data model](creating-a-core-data-model.md)
  Define your app’s object structure with a data model file.
- [Setting up a Core Data stack](setting-up-a-core-data-stack.md)
  Set up the classes that manage and persist your app’s objects.
- [Handling Different Data Types in Core Data](handling-different-data-types-in-core-data.md)
  Create, store, and present records for a variety of data types.
- [Linking Data Between Two Core Data Stores](linking-data-between-two-core-data-stores.md)
  Organize data in two different stores and implement a link between them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/core-data-stack)*