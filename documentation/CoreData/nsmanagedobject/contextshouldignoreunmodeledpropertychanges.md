# contextShouldIgnoreUnmodeledPropertyChanges

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var contextShouldIgnoreUnmodeledPropertyChanges: Bool { get }
```

```objc
@property (class, readonly) BOOL contextShouldIgnoreUnmodeledPropertyChanges;
```

## Return Value

[`false`](../../Swift/false.md) if instances of the class should be marked as having changes if an unmodeled property is changed, otherwise [`true`](../../Swift/true.md).

## Discussion

The default value is [`true`](../../Swift/true.md).

## See Also

### Related Documentation
- [var hasChanges: Bool](../nsmanagedobjectcontext/haschanges.md)
  A Boolean value that indicates whether the context has uncommitted changes.
### Managing Change Events
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
- [func didTurnIntoFault()](./didturnintofault%28%29.md)
  Provides an opportunity to add code into the life cycle of the managed object after converting it to a fault.
- [class func fetchRequest() -> NSFetchRequest<any NSFetchRequestResult>](./fetchrequest%28%29.md)
  Returns an initialized fetch request with the entity this subclass represents.
- [+ fetchRequest](./fetchrequest.md)
  Returns an initialized fetch request with the entity this subclass represents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/contextshouldignoreunmodeledpropertychanges)*