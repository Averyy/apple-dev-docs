# didTurnIntoFault()

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to add code into the life cycle of the managed object after converting it to a fault.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func didTurnIntoFault()
```

```objc
- (void) didTurnIntoFault;
```

## Discussion

You use this method to clear out custom data caches—transient values declared as entity properties are typically already cleared out by the time this method is invoked (see, for example, [`refresh(_:mergeChanges:)`](../nsmanagedobjectcontext/refresh%28_,mergechanges%29.md)).

## See Also

### Managing Change Events
- [class var contextShouldIgnoreUnmodeledPropertyChanges: Bool](./contextshouldignoreunmodeledpropertychanges.md)
  A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.
- [func awakeFromFetch()](./awakefromfetch%28%29.md)
  Provides an opportunity to add code into the life cycle of the managed object when fufilling it from a fault.
- [func awakeFromInsert()](./awakefrominsert%28%29.md)
  Provides an opportunity to add code into the life cycle of the managed object when initially creating it.
- [func awake(fromSnapshotEvents: NSSnapshotEventType)](./awake%28fromsnapshotevents%29.md)
  Provides an opportunity to add code into the life cycle of the managed object when fulfilling it from a snapshot.
- [func changedValues() -> [String : Any]](./changedvalues%28%29.md)
  Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.
- [func changedValuesForCurrentEvent() -> [String : Any]](./changedvaluesforcurrentevent%28%29.md)
  Returns a dictionary containing the keys and new values of persistent properties with changes since the last fetching or saving of the managed object.
- [func committedValues(forKeys: [String]?) -> [String : Any]](./committedvalues%28forkeys%29.md)
  Returns a dictionary of the most recent fetched or saved values of the managed object for the properties of the specified keys.
- [func prepareForDeletion()](./preparefordeletion%28%29.md)
  Provides an opportunity to add code into the life cycle of the managed object before deleting it.
- [func willSave()](./willsave%28%29.md)
  Provides an opportunity to add code into the life cycle of the managed object before saving it.
- [func didSave()](./didsave%28%29.md)
  Provides an opportunity to add code into the life cycle of the managed object after the managed object’s context completes a save operation.
- [func willTurnIntoFault()](./willturnintofault%28%29.md)
  Provides an opportunity to add code into the life cycle of the managed object before converting it to a fault.
- [class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>](./fetchrequest%28%29.md)
  Returns an initialized fetch request with the entity this subclass represents.
- [+ fetchRequest](./fetchrequest.md)
  Returns an initialized fetch request with the entity this subclass represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/didturnintofault())*