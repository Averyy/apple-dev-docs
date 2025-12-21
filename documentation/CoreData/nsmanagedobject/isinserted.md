# isInserted

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the managed object has been inserted in a managed object context.

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
var isInserted: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver has been inserted in a managed object context, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

- [var managedObjectContext: NSManagedObjectContext?](nsmanagedobject/managedobjectcontext.md)
  The managed object context with which the managed object is registered.
- [var hasChanges: Bool](nsmanagedobject/haschanges.md)
  A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/isinserted)*