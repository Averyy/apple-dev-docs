# willTurnIntoFault()

**Framework**: Core Data  
**Kind**: method

Provides an opportunity to add code into the life cycle of the managed object before converting it to a fault.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func willTurnIntoFault()
```

#### Discussion

This method is the companion of the [`didTurnIntoFault()`](nsmanagedobject/didturnintofault().md) method. You can use it to (re)set state which requires access to property values (for example, observers across key paths). The default implementation does nothing.

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
- [func didTurnIntoFault()](nsmanagedobject/didturnintofault.md)
  Provides an opportunity to add code into the life cycle of the managed object after converting it to a fault.
- [class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>](nsmanagedobject/fetchrequest.md)
  Returns an initialized fetch request with the entity this subclass represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/willturnintofault())*