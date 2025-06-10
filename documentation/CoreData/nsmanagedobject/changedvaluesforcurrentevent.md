# changedValuesForCurrentEvent()

**Framework**: Core Data  
**Kind**: method

Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func changedValuesForCurrentEvent() -> [String : Any]
```

#### Return Value

A dictionary with keys that are the names of persistent properties with changes since the last posting of [`NSManagedObjectContextObjectsDidChange`](https://developer.apple.com/documentation/Foundation/NSNotification/Name-swift.struct/NSManagedObjectContextObjectsDidChange), and with the new values for those properties.

#### Discussion

This method only reports changes to properties that are persistent properties of the receiver, not changes to transient properties or custom instance variables.

> **Note**: In Objective-C, this method returns the keys and values of persistent properties with changes since the last posting of [`NSManagedObjectContextObjectsDidChangeNotification`](nsmanagedobjectcontextobjectsdidchangenotification.md).

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/changedvaluesforcurrentevent())*