# hasFault(forRelationshipNamed:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the relationship for a given key is a fault.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func hasFault(forRelationshipNamed key: String) -> Bool
```

```objc
- (BOOL) hasFaultForRelationshipNamed:(NSString *) key;
```

## Return Value

[`true`](../../Swift/true.md) if the relationship for `key` is a fault; otherwise, [`false`](../../Swift/false.md).

## Discussion

If the specified relationship is a fault, calling this method does not result in the fault firing.

## Parameters

- `key`: The name of one of the receiver’s relationships.

## See Also

### Getting State Information
- [var managedObjectContext: NSManagedObjectContext?](./managedobjectcontext.md)
  The managed object context with which the managed object is registered.
- [var hasChanges: Bool](./haschanges.md)
  A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
- [var isInserted: Bool](./isinserted.md)
  A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [var isUpdated: Bool](./isupdated.md)
  A Boolean value that indicates whether the managed object has unsaved changes.
- [var isDeleted: Bool](./isdeleted.md)
  A Boolean value that indicates whether the managed object will be deleted during the next save.
- [var isFault: Bool](./isfault.md)
  A Boolean value that indicates whether the managed object is a fault.
- [var faultingState: Int](./faultingstate.md)
  The faulting state of the managed object.
- [var hasPersistentChangedValues: Bool](./haspersistentchangedvalues.md)
  A Boolean value that indicates whether the managed object has persistent changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/hasfault(forrelationshipnamed:))*