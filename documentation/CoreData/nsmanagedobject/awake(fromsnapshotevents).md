# awake(fromSnapshotEvents:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity to add code into the life cycle of the managed object when fulfilling it from a snapshot.

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
func awake(fromSnapshotEvents flags: NSSnapshotEventType)
```

```objc
- (void) awakeFromSnapshotEvents:(NSSnapshotEventType) flags;
```

#### Discussion

You typically use this method to compute derived values or to recreate transient relationships from the receiver’s persistent properties.

If you want to set attribute values and need to avoid emitting key-value observation change notifications, you should use primitive accessor methods (either [`setPrimitiveValue(_:forKey:)`](./setprimitivevalue%28_,forkey%29.md) or—better—the appropriate custom primitive accessors). This ensures that the new values are treated as baseline values rather than being recorded as undoable changes for the properties in question.

> ❗ **Important**:  Subclasses must invoke super’s implementation before performing their own initialization.

## Parameters

- `flags`: A bit mask of [`didChangeValue(forKey:)`](./didchangevalue%28forkey%29.md) constants to denote the event or events that led to the method being invoked.

  For possible values, see [`NSSnapshotEventType`](../nssnapshoteventtype.md).

## See Also

### Managing Change Events
- [class var contextShouldIgnoreUnmodeledPropertyChanges: Bool](./contextshouldignoreunmodeledpropertychanges.md)
  A Boolean value that indicates whether to mark instances of the class as having changes when an unmodeled property changes.
- [func awakeFromFetch()](./awakefromfetch%28%29.md)
  Provides an opportunity to add code into the life cycle of the managed object when fufilling it from a fault.
- [func awakeFromInsert()](./awakefrominsert%28%29.md)
  Provides an opportunity to add code into the life cycle of the managed object when initially creating it.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/awake(fromsnapshotevents:))*