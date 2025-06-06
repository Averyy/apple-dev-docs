# CLSDataStore

**Framework**: ClassKit  
**Kind**: class

A container for all the ClassKit data in your app.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 11.3+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CLSDataStore
```

#### Overview

Use the ClassKit data store to build and access contexts ([`CLSContext`](clscontext.md) instances) that you use to advertise your app’s assignable content. Contexts in turn provide access to activities ([`CLSActivity`](clsactivity.md) instances) and activity items ([`CLSScoreItem`](clsscoreitem.md), [`CLSBinaryItem`](clsbinaryitem.md), and [`CLSQuantityItem`](clsquantityitem.md) instances) that you use to record progress through assignments. You don’t instantiate a data store yourself. Instead, use the single [`shared`](clsdatastore/shared.md) data store instance throughout your app.

The data store provides access to the app’s one and only main context through the [`mainAppContext`](clsdatastore/mainappcontext.md) property. This property acts as the root context in your context hierarchy that you can use as a starting point when searching for descendant contexts.

To build contexts, you adopt the [`CLSDataStoreDelegate`](clsdatastoredelegate.md) protocol in one of your classes, typically one that exists for the lifetime of your app, and assign an instance of that class as the shared data store’s [`delegate`](clsdatastore/delegate.md) property. Then, when the data store needs a context that it’s never seen before, it asks your delegate to build it.

After you make changes to any context, activity, or activity item, call the data store’s [`save(completion:)`](clsdatastore/save(completion:).md) method to commit the changes, and propagate them through the network.

## Topics

### Accessing the shared data store
- [class var shared: CLSDataStore](clsdatastore/shared.md)
  The shared data store object.
### Managing the delegate
- [Building missing contexts](building-missing-contexts.md)
  Create and initialize missing contexts.
- [var delegate: (any CLSDataStoreDelegate)?](clsdatastore/delegate.md)
  The data store delegate instance.
- [protocol CLSDataStoreDelegate](clsdatastoredelegate.md)
  An interface the data store uses to request new contexts.
### Accessing specific contexts and activities
- [var mainAppContext: CLSContext](clsdatastore/mainappcontext.md)
  The app’s top-level context.
- [var activeContext: CLSContext?](clsdatastore/activecontext.md)
  The currently active context.
- [var runningActivity: CLSActivity?](clsdatastore/runningactivity.md)
  The currently running activity within the currently active context.
- [func fetchActivity(for: URL, completion: (CLSActivity?, (any Error)?) -> Void)](clsdatastore/fetchactivity(for:completion:).md)
  Fetches an activity for a given document so you can record progress on the associated task.
- [func completeAllAssignedActivities(matching: [String])](clsdatastore/completeallassignedactivities(matching:).md)
  Marks all of the assigned and active activities for the given context path as complete.
### Finding contexts that match criteria
- [func contexts(matchingIdentifierPath: [String], completion: ([CLSContext], (any Error)?) -> Void)](clsdatastore/contexts(matchingidentifierpath:completion:).md)
  Fetches all the contexts along a given identifier path.
- [func contexts(matching: NSPredicate, completion: ([CLSContext], (any Error)?) -> Void)](clsdatastore/contexts(matching:completion:).md)
  Fetches all the contexts matching a predicate.
- [struct CLSPredicateKeyPath](clspredicatekeypath.md)
  The set of possible key paths you use to search for contexts.
### Removing contexts
- [func remove(CLSContext)](clsdatastore/remove(_:).md)
  Marks a context for removal.
### Saving changes
- [func save(completion: (((any Error)?) -> Void)?)](clsdatastore/save(completion:).md)
  Saves any changes you’ve made in the data store.

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

- [Enabling ClassKit in your app](enabling-classkit-in-your-app.md)
  Prepare your app and your development environment to adopt ClassKit.
- [ClassKit Environment Entitlement](../BundleResources/Entitlements/com.apple.developer.ClassKit-environment.md)
  The ClassKit development or production environment for an education app that works with the Schoolwork app.
- [Incorporating ClassKit into an Educational App](incorporating-classkit-into-an-educational-app.md)
  Walk through the process of setting up assignments and recording student progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkit/clsdatastore)*