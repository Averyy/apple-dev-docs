# hasChanges

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var hasChanges: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasChanges;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver has been inserted, has been deleted, or has unsaved changes, otherwise [`false`](../../Swift/false.md). The result is the equivalent of OR-ing the values of [`isInserted`](./isinserted.md), [`isDeleted`](./isdeleted.md), and [`isUpdated`](./isupdated.md).

## See Also

### Getting State Information
- [var managedObjectContext: NSManagedObjectContext?](./managedobjectcontext.md)
  The managed object context with which the managed object is registered.
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
- [func hasFault(forRelationshipNamed: String) -> Bool](./hasfault%28forrelationshipnamed%29.md)
  Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [var hasPersistentChangedValues: Bool](./haspersistentchangedvalues.md)
  A Boolean value that indicates whether the managed object has persistent changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/haschanges)*