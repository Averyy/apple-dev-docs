# awakeFromFetch()

**Framework**: Core Data  
**Kind**: method

Provides an opportunity to add code into the life cycle of the managed object when fufilling it from a fault.

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
func awakeFromFetch()
```

#### Discussion

You typically use this method to compute derived values or to recreate transient relationships from the receiver’s persistent properties.

The managed object context’s change processing is explicitly disabled around this method so that you can use public setters to establish transient values and other caches without dirtying the object or its context. Because of this, however, you should not modify relationships in this method as the inverse will not be set.

> ❗ **Important**:  Subclasses must invoke super’s implementation before performing their own initialization.

## See Also

- [func setPrimitiveValue(Any?, forKey: String)](nsmanagedobject/setprimitivevalue(_:forkey:).md)
  Sets the value of a given property in the managed object’s private internal storage.
- [func primitiveValue(forKey: String) -> Any?](nsmanagedobject/primitivevalue(forkey:).md)
  Returns the value for the specified property from the managed object’s private internal storage .
- [class var contextShouldIgnoreUnmodeledPropertyChanges: Bool](nsmanagedobject/contextshouldignoreunmodeledpropertychanges.md)
  A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/awakefromfetch())*