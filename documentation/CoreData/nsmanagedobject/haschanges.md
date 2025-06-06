# hasChanges

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.

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
var hasChanges: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver has been inserted, has been deleted, or has unsaved changes, otherwise [`false`](https://developer.apple.com/documentation/swift/false). The result is the equivalent of OR-ing the values of [`isInserted`](nsmanagedobject/isinserted.md), [`isDeleted`](nsmanagedobject/isdeleted.md), and [`isUpdated`](nsmanagedobject/isupdated.md).

## See Also

- [var managedObjectContext: NSManagedObjectContext?](nsmanagedobject/managedobjectcontext.md)
  The managed object context with which the managed object is registered.
- [var isInserted: Bool](nsmanagedobject/isinserted.md)
  A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [var isUpdated: Bool](nsmanagedobject/isupdated.md)
  A Boolean value that indicates whether the managed object has unsaved changes.
- [var isDeleted: Bool](nsmanagedobject/isdeleted.md)
  A Boolean value that indicates whether the managed object will be deleted during the next save.
- [var isFault: Bool](nsmanagedobject/isfault.md)
  A Boolean value that indicates whether the managed object is a fault.
- [var faultingState: Int](nsmanagedobject/faultingstate.md)
  The faulting state of the managed object.
- [func hasFault(forRelationshipNamed: String) -> Bool](nsmanagedobject/hasfault(forrelationshipnamed:).md)
  Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [var hasPersistentChangedValues: Bool](nsmanagedobject/haspersistentchangedvalues.md)
  A Boolean value that indicates whether the managed object has persistent changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/haschanges)*