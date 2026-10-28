# committedValues(forKeys:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary of the most recent fetched or saved values of the managed object for the properties of the specified keys.

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
func committedValues(forKeys keys: [String]?) -> [String : Any]
```

```objc
- (NSDictionary<NSString *,id> *) committedValuesForKeys:(NSArray<NSString *> *) keys;
```

## Return Value

A dictionary containing the last fetched or saved values of the receiver for the properties specified by `keys`.

## Discussion

`nil` values are represented by an instance of [`NSNull`](../../Foundation/nsnull.md).

This method only reports values of properties that are defined as persistent properties of the receiver, not values of transient properties or of custom instance variables.

You can invoke this method with the `keys` value of `nil` to retrieve committed values for all the receiver’s properties, as illustrated by the following example.

```objc
NSDictionary *allCommittedValues =
        [aManagedObject committedValuesForKeys:nil];
```

It is more efficient to use `nil` than to pass an array of all the property keys.

## Parameters

- `keys`: An array containing names of properties of the receiver, or `nil`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/committedvalues(forkeys:))*