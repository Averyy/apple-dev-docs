# awakeFromInsert()

**Framework**: Core Data  
**Kind**: method

Provides an opportunity to add code into the life cycle of the managed object when initially creating it.

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
func awakeFromInsert()
```

#### Discussion

You typically use this method to initialize special default property values. This method is invoked only once in the object’s lifetime.

If you want to set attribute values in an implementation of this method, you should typically use primitive accessor methods (either [`setPrimitiveValue(_:forKey:)`](nsmanagedobject/setprimitivevalue(_:forkey:).md) or—better—the appropriate custom primitive accessors). This ensures that the new values are treated as baseline values rather than being recorded as undoable changes for the properties in question.

> ❗ **Important**:  Subclasses must invoke super’s implementation before performing their own initialization.

##### Special Considerations

If you create a managed object then perform undo operations to bring the managed object context to a state prior to the object’s creation, then perform redo operations to bring the managed object context back to a state after the object’s creation, [`awakeFromInsert()`](nsmanagedobject/awakefrominsert().md) is  invoked a second time.

You are typically discouraged from performing fetches within an implementation of [`awakeFromInsert()`](nsmanagedobject/awakefrominsert().md). Although it is allowed, execution of the fetch request can trigger the sending of internal Core Data notifications which may have unwanted side-effects. For example, in macOS, an instance of [`NSArrayController`](https://developer.apple.com/documentation/AppKit/NSArrayController) may end up inserting a new object into its content array twice.

## See Also

- [class var contextShouldIgnoreUnmodeledPropertyChanges: Bool](nsmanagedobject/contextshouldignoreunmodeledpropertychanges.md)
  A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.
- [func awakeFromFetch()](nsmanagedobject/awakefromfetch.md)
  Provides an opportunity to add code into the life cycle of the managed object when fufilling it from a fault.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/awakefrominsert())*