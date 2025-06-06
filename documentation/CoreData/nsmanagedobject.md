# NSManagedObject

**Framework**: Coredata  
**Kind**: class

The base class that all Core Data model objects inherit from.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSManagedObject
```

## Mentions

- [Syncing a Core Data Store with CloudKit](syncing-a-core-data-store-with-cloudkit.md)
- [Modeling data](modeling-data.md)
- [Generating code](generating-code.md)
- [Using Core Data in the background](using-core-data-in-the-background.md)

#### Overview

A managed object has an associated entity description ([`NSEntityDescription`](nsentitydescription.md)) that provides metadata about the object, including the name of the entity that the object represents and the names of its attributes and relationships. A managed object also has an associated managed object context that tracks changes to the object graph.

You can’t use instances of direct subclasses of [`NSObject`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class), or any other class that doesn’t inherit from [`NSManagedObject`](nsmanagedobject.md), with a managed object context. You may create custom subclasses of [`NSManagedObject`](nsmanagedobject.md), although this isn’t always necessary. If you don’t need custom logic, you can create a complete object graph with [`NSManagedObject`](nsmanagedobject.md) instances.

If you instantiate a managed object directly, you must call the designated initializer [`init(entity:insertInto:)`](nsmanagedobject/init(entity:insertinto:).md).

##### Data Storage

In some respects, an `NSManagedObject` acts like a dictionary—it’s a generic container object that provides efficient storage for the properties defined by its associated `NSEntityDescription` instance. `NSManagedObject` supports a range of common types for attribute values, including string, date, and number (see [`NSAttributeDescription`](nsattributedescription.md) for full details). Therefore, typically you don’t need to define instance variables in subclasses. Sometimes, however, you want to use types that aren’t supported directly, such as colors and C structures. For example, in a graphics application you might want to define a Rectangle entity that has color and bounds attributes that are an instance of `NSColor` and an `NSRect` struct, respectively. For some types you can use a transformable attribute, for others this may require you to create a subclass of `NSManagedObject`.

> **Note**: The default value for [`automaticallyNotifiesObservers(forKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/automaticallyNotifiesObservers(forKey:)) is `false` for managed properties of a `NSManagedObject`, and `true` for unmanaged properties.

##### Faulting

Managed objects typically represent data held in a persistent store. In some situations a managed object may be a —an object whose property values haven’t yet been loaded from the external data store. When you access persistent property values, the fault “fires” and the data is retrieved from the store automatically. This can be a comparatively expensive process (potentially requiring a round trip to the persistent store), and you may wish to avoid unnecessarily firing a fault. See [`Faulting and Uniquing`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/FaultingandUniquing.html#//apple_ref/doc/uid/TP40001075-CH18) for more details on faults.

You can safely invoke the following methods and properties on a fault without causing it to fire: [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)), [`hash`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/hash), [`superclass`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/superclass), [`class`](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1571949-class), [`self()`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/self()), [`isProxy()`](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418528-isproxy), [`isKind(of:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isKind(of:)), [`isMember(of:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isMember(of:)), [`conforms(to:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/conforms(to:)), [`responds(to:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/responds(to:)), [`description`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/description), [`managedObjectContext`](nsmanagedobject/managedobjectcontext.md), [`entity`](nsmanagedobject/entity-swift.property.md), [`objectID`](nsmanagedobject/objectid.md), [`isInserted`](nsmanagedobject/isinserted.md), [`isUpdated`](nsmanagedobject/isupdated.md), [`isDeleted`](nsmanagedobject/isdeleted.md), [`faultingState`](nsmanagedobject/faultingstate.md), and [`isFault`](nsmanagedobject/isfault.md). Because `isEqual` and `hash` don’t cause a fault to fire, managed objects can typically be placed in collections without firing a fault. Note, however, that invoking key-value coding methods on the collection object might in turn result in an invocation of `valueForKey:` on a managed object, which would fire the fault.

Although the `description` property doesn’t cause a fault to fire, if you implement a custom `description` that accesses the object’s persistent properties, this does cause a fault to fire. You are strongly discouraged from overriding `description` in this way.

##### Subclassing Notes

In combination with the entity description in the managed object model, `NSManagedObject` provides a rich set of default behaviors including support for arbitrary properties and value validation. If you decide to subclass `NSManagedObject` to implement custom features, make sure you don’t disrupt Core Data’s behavior.

###### Methods and Properties You Must Not Override

`NSManagedObject` itself customizes many features of `NSObject` so that managed objects can be properly integrated into the Core Data infrastructure. Core Data relies on the `NSManagedObject` implementation of the following methods and properties, which you therefore absolutely must not override: [`primitiveValue(forKey:)`](nsmanagedobject/primitivevalue(forkey:).md), [`setPrimitiveValue(_:forKey:)`](nsmanagedobject/setprimitivevalue(_:forkey:).md), [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)), [`hash`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/hash), [`superclass`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/superclass), [`class`](https://developer.apple.com/documentation/objectivec/1418956-nsobject/1571949-class), [`self()`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/self()), [`isProxy()`](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/1418528-isproxy), [`isKind(of:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isKind(of:)), [`isMember(of:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isMember(of:)), [`conforms(to:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/conforms(to:)), [`responds(to:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/responds(to:)), [`managedObjectContext`](nsmanagedobject/managedobjectcontext.md), [`entity`](nsmanagedobject/entity-swift.property.md), [`objectID`](nsmanagedobject/objectid.md), [`isInserted`](nsmanagedobject/isinserted.md), [`isUpdated`](nsmanagedobject/isupdated.md), [`isDeleted`](nsmanagedobject/isdeleted.md), and [`isFault`](nsmanagedobject/isfault.md), [`alloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571958-alloc), [`allocWithZone:`](https://developer.apple.com/documentation/objectivec/nsobject/1571945-allocwithzone), [`new`](https://developer.apple.com/documentation/objectivec/nsobject/1571948-new),  [`instancesRespond(to:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/instancesRespond(to:)), [`instanceMethod(for:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/instanceMethod(for:)), [`method(for:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/method(for:)), [`methodSignatureForSelector:`](https://developer.apple.com/documentation/objectivec/nsobject/1571960-methodsignatureforselector), [`instanceMethodSignatureForSelector:`](https://developer.apple.com/documentation/objectivec/nsobject/1571959-instancemethodsignatureforselect), or [`isSubclass(of:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/isSubclass(of:)).

###### Methods and Properties You Shouldnt Override

As with any class, you are strongly discouraged from overriding the key-value observing methods such as [`willChangeValue(forKey:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/willChangeValue(forKey:)) and [`didChangeValue(forKey:withSetMutation:using:)`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/didChangeValue(forKey:withSetMutation:using:)). Avoid overriding `description`—if this method fires a fault during a debugging operation, the results may be unpredictable. Also avoid overriding [`init(entity:insertInto:)`](nsmanagedobject/init(entity:insertinto:).md), or `dealloc`. Changing values in the [`init(entity:insertInto:)`](nsmanagedobject/init(entity:insertinto:).md) method won’t be noticed by the context, and if you aren’t careful, those changes may not be saved. Perform most initialization customization in one of the `awake…` methods. If you do override [`init(entity:insertInto:)`](nsmanagedobject/init(entity:insertinto:).md), make sure you adhere to the requirements set out in the method description. See [`init(entity:insertInto:)`](nsmanagedobject/init(entity:insertinto:).md).

Don’t override `dealloc` because [`didTurnIntoFault()`](nsmanagedobject/didturnintofault().md) is usually a better time to clear values—a managed object may not be reclaimed for some time after it has been turned into a fault. Core Data doesn’t guarantee that `dealloc` will be called in all scenarios (such as when the application quits). Therefore, don’t include required side effects (like saving or changes to the file system, user preferences, and so on) in these methods.

In summary, for [`init(entity:insertInto:)`](nsmanagedobject/init(entity:insertinto:).md) and `dealloc`, Core Data reserves exclusive control over the life cycle of the managed object (that is, raw memory management). This is so that the framework can provide features such as uniquing and by consequence, relationship maintenance, as well as much better performance than would be possible otherwise.

###### Additional Override Considerations

The following methods are intended to be fine grained and aren’t suitable for large-scale operations. Don’t fetch or save in these methods. In particular, they shouldn’t have side effects on the managed object context.

- [`init(entity:insertInto:)`](nsmanagedobject/init(entity:insertinto:).md)
- [`didTurnIntoFault()`](nsmanagedobject/didturnintofault().md)
- [`willTurnIntoFault()`](nsmanagedobject/willturnintofault().md)
- `dealloc`

In addition, if you plan to override `awakeFromInsert`, `awakeFromFetch`, and validation methods, first invoke `super.method()`, the superclass’s implementation. Don’t modify relationships in [`awakeFromFetch()`](nsmanagedobject/awakefromfetch().md)—see the method description for details.

###### Custom Accessor Methods

Typically, you don’t need to write custom accessor methods for properties that are defined in the entity of a managed object’s corresponding managed object model. If you need to do so, follow the implementation patterns described in Managed Object Accessor Methods in [`Core Data Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075).

Core Data automatically generates accessor methods (and primitive accessor methods) for you. For attributes and to-one relationships, Core Data generates the standard get and set accessor methods; for to-many relationships, Core Data generates the indexed accessor methods as described in [`Achieving Basic Key-Value Coding Compliance`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/AccessorConventions.html#//apple_ref/doc/uid/20002174) in [`Key-Value Coding Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i). You do however need to declare the accessor methods or use Objective-C properties to suppress compiler warnings. For a full discussion, see Managed Object Accessor Methods in [`Core Data Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075).

###### Custom Instance Variables

By default, `NSManagedObject` stores its properties in an internal structure as objects, and in general Core Data is more efficient working with storage under its own control rather than by using custom instance variables.

`NSManagedObject` provides support for a range of common types for attribute values, including string, date, and number (see [`NSAttributeDescription`](nsattributedescription.md) for full details). If you want to use types that aren’t supported directly, like colors and C structures, you can either use transformable attributes or create a subclass of `NSManagedObject`.

Sometimes it’s convenient to represent variables as scalars—in drawing applications, for example, where variables represent dimensions and x and y coordinates and are frequently used in calculations. To represent attributes as scalars, you declare instance variables as you do in any other class. You also need to implement suitable accessor methods as described in Managed Object Accessor Methods.

If you define custom instance variables for example to store derived attributes or other transient properties, clean up these variables in [`didTurnIntoFault()`](nsmanagedobject/didturnintofault().md) rather than `dealloc`.

###### Validation Methods

`NSManagedObject` provides consistent hooks for validating property and inter-property values. You typically shouldn’t override [`validateValue(_:forKey:)`](nsmanagedobject/validatevalue(_:forkey:).md). Instead implement methods of the form `validate<Key>:error:`, as defined by the NSKeyValueCoding protocol. If you want to validate inter-property values, you can override [`validateForUpdate()`](nsmanagedobject/validateforupdate().md) and/or related validation methods.

Don’t call `validateValue:forKey:error:` within custom property validation methods—if you do, you create an infinite loop when `validateValue:forKey:error:` is invoked at runtime. If you do implement custom validation methods, don’t call them directly. Instead, call `validateValue:forKey:error:` with the appropriate key. This ensures that any constraints defined in the managed object model are applied.

If you implement custom inter-property validation methods like [`validateForUpdate()`](nsmanagedobject/validateforupdate().md), call the superclass’s implementation first. This ensures that individual property validation methods are also invoked. If there are multiple validation failures in one operation, collect them in an array and add the array—using the key `NSDetailedErrorsKey`—to the userInfo dictionary in the `NSError` object you return. For an example, see Managed Object Validation.

## Topics

### Creating a Managed Object
- [init(entity: NSEntityDescription, insertInto: NSManagedObjectContext?)](nsmanagedobject/init(entity:insertinto:).md)
  Initializes a managed object from an entity description and inserts it into the specified managed object context.
- [convenience init(context: NSManagedObjectContext)](nsmanagedobject/init(context:).md)
  Initializes a managed object subclass and inserts it into the specified managed object context.
### Getting a Managed Object’s Identity
- [var entity: NSEntityDescription](nsmanagedobject/entity-swift.property.md)
  The entity description of the managed object.
- [var objectID: NSManagedObjectID](nsmanagedobject/objectid.md)
  The object ID of the managed object.
- [class func entity() -> NSEntityDescription](nsmanagedobject/entity.md)
  Returns the entity description that is associated with this subclass.
### Getting State Information
- [var managedObjectContext: NSManagedObjectContext?](nsmanagedobject/managedobjectcontext.md)
  The managed object context with which the managed object is registered.
- [var hasChanges: Bool](nsmanagedobject/haschanges.md)
  A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
- [var isInserted: Bool](nsmanagedobject/isinserted.md)
  A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [var isUpdated: Bool](nsmanagedobject/isupdated.md)
  A Boolean value that indicates whether the managed object has unsaved changes.
- [var isDeleted: Bool](nsmanagedobject/isdeleted.md)
  A Boolean value that indicates whether the managed object will be deleted during the next save.
- [var isFault: Bool](nsmanagedobject/isfault.md)
  A Boolean value that indicates whether the managed object is a fault.
- [var faultingState: Int](nsmanagedobject/faultingstate.md)
  The faulting state of the managed object.
- [func hasFault(forRelationshipNamed: String) -> Bool](nsmanagedobject/hasfault(forrelationshipnamed:).md)
  Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [var hasPersistentChangedValues: Bool](nsmanagedobject/haspersistentchangedvalues.md)
  A Boolean value that indicates whether the managed object has persistent changes.
### Managing Change Events
- [class var contextShouldIgnoreUnmodeledPropertyChanges: Bool](nsmanagedobject/contextshouldignoreunmodeledpropertychanges.md)
  A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.
- [func awakeFromFetch()](nsmanagedobject/awakefromfetch.md)
  Provides an opportunity to add code into the life cycle of the managed object when fufilling it from a fault.
- [func awakeFromInsert()](nsmanagedobject/awakefrominsert.md)
  Provides an opportunity to add code into the life cycle of the managed object when initially creating it.
- [func awake(fromSnapshotEvents: NSSnapshotEventType)](nsmanagedobject/awake(fromsnapshotevents:).md)
  Provides an opportunity to add code into the life cycle of the managed object when fulfilling it from a snapshot.
- [func changedValues() -> [String : Any]](nsmanagedobject/changedvalues.md)
  Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.
- [func changedValuesForCurrentEvent() -> [String : Any]](nsmanagedobject/changedvaluesforcurrentevent.md)
  Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.
- [func committedValues(forKeys: [String]?) -> [String : Any]](nsmanagedobject/committedvalues(forkeys:).md)
  Returns a dictionary of the most recent fetched or saved values of the managed object for the properties of the specified keys.
- [func prepareForDeletion()](nsmanagedobject/preparefordeletion.md)
  Provides an opportunity to add code into the life cycle of the managed object before deleting it.
- [func willSave()](nsmanagedobject/willsave.md)
  Provides an opportunity to add code into the life cycle of the managed object before saving it.
- [func didSave()](nsmanagedobject/didsave.md)
  Provides an opportunity to add code into the life cycle of the managed object after the managed object’s context completes a save operation.
- [func willTurnIntoFault()](nsmanagedobject/willturnintofault.md)
  Provides an opportunity to add code into the life cycle of the managed object before converting it to a fault.
- [func didTurnIntoFault()](nsmanagedobject/didturnintofault.md)
  Provides an opportunity to add code into the life cycle of the managed object after converting it to a fault.
- [class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>](nsmanagedobject/fetchrequest.md)
  Returns an initialized fetch request with the entity this subclass represents.
### Supporting Key-Value Coding
- [func value(forKey: String) -> Any?](nsmanagedobject/value(forkey:).md)
  Returns the value for the property specified by `key`.
- [func setValue(Any?, forKey: String)](nsmanagedobject/setvalue(_:forkey:).md)
  Sets the specified property of the managed object to the specified value.
- [func primitiveValue(forKey: String) -> Any?](nsmanagedobject/primitivevalue(forkey:).md)
  Returns the value for the specified property from the managed object’s private internal storage .
- [func setPrimitiveValue(Any?, forKey: String)](nsmanagedobject/setprimitivevalue(_:forkey:).md)
  Sets the value of a given property in the managed object’s private internal storage.
- [func objectIDs(forRelationshipNamed: String) -> [NSManagedObjectID]](nsmanagedobject/objectids(forrelationshipnamed:).md)
  Returns the object IDs for all of the managed objects that are in the named relationship.
### Managing Data Validation
- [func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](nsmanagedobject/validatevalue(_:forkey:).md)
  Validates a property value for a given key.
- [func validateForDelete() throws](nsmanagedobject/validatefordelete.md)
  Determines whether the managed object can be deleted in its current state.
- [func validateForInsert() throws](nsmanagedobject/validateforinsert.md)
  Determines whether the managed object can be inserted in its current state.
- [func validateForUpdate() throws](nsmanagedobject/validateforupdate.md)
  Determines whether the managed object’s current state is valid.
- [Validation error codes](1535452-validation-error-codes.md)
  Error codes relating to the validation of managed objects.
- [let NSValidationKeyErrorKey: String](nsvalidationkeyerrorkey.md)
  The error key for the attribute that failed to validate.
- [let NSValidationObjectErrorKey: String](nsvalidationobjecterrorkey.md)
  The error key for the object that failed to validate.
- [let NSValidationPredicateErrorKey: String](nsvalidationpredicateerrorkey.md)
  The error key for the predicate that failed to validate.
- [let NSValidationValueErrorKey: String](nsvalidationvalueerrorkey.md)
  The error key for the value that failed to validate.
### Supporting Key-Value Observing
- [func didAccessValue(forKey: String?)](nsmanagedobject/didaccessvalue(forkey:).md)
  Provides support for key-value observing access notification.
- [func observationInfo() -> UnsafeMutableRawPointer?](nsmanagedobject/observationinfo.md)
  Returns the observation info of the managed object.
- [func setObservationInfo(UnsafeMutableRawPointer?)](nsmanagedobject/setobservationinfo(_:).md)
  Sets the observation info of the managed object.
- [func willAccessValue(forKey: String?)](nsmanagedobject/willaccessvalue(forkey:).md)
  Provides support for key-value observing access notification.
- [func didChangeValue(forKey: String)](nsmanagedobject/didchangevalue(forkey:).md)
  Provides an opportunity to respond when a value of a given property has changed.
- [func didChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](nsmanagedobject/didchangevalue(forkey:withsetmutation:using:).md)
  Provides an opportunity to respond when a change was made to a specified to-many relationship.
- [func willChangeValue(forKey: String)](nsmanagedobject/willchangevalue(forkey:).md)
  Provides an opportunity to respond when a value of a given property is about to change.
- [func willChangeValue(forKey: String, withSetMutation: NSKeyValueSetMutationKind, using: Set<AnyHashable>)](nsmanagedobject/willchangevalue(forkey:withsetmutation:using:).md)
  Provides an opportunity to respond when a change is about to be made to a specified to-many relationship.
### Reinitializing Values
- [struct NSSnapshotEventType](nssnapshoteventtype.md)
  Constants that specify the reason the managed object may need to reinitialize its values.
### Subscripts
- [subscript(String) -> Any?](nsmanagedobject/subscript(_:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSFetchRequestResult](nsfetchrequestresult.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ObservableObject](../Combine/ObservableObject.md)

## See Also

- [class NSEntityDescription](nsentitydescription.md)
  A description of a Core Data entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreData/nsmanagedobject)*