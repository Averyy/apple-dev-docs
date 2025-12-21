# isFault

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the managed object is a fault.

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
var isFault: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver is a fault, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). Knowing whether an object is a fault is useful in many situations when computations are optional. It can also be used to avoid growing the object graph unnecessarily (which may improve performance as it can avoid time-consuming fetches from data stores).

If this property is [`false`](https://developer.apple.com/documentation/Swift/false), then the receiver’s data must be in memory. However, if this property is  [`true`](https://developer.apple.com/documentation/Swift/true), it does  mean that the data is not in memory. The data may be in memory, or it may not, depending on many factors influencing caching.

If the receiver is a fault, accessing this property does not cause it to fire.

## See Also

- [var managedObjectContext: NSManagedObjectContext?](nsmanagedobject/managedobjectcontext.md)
  The managed object context with which the managed object is registered.
- [var hasChanges: Bool](nsmanagedobject/haschanges.md)
  A Boolean value that indicates whether the managed object has been inserted, has been deleted, or has unsaved changes.
- [var isInserted: Bool](nsmanagedobject/isinserted.md)
  A Boolean value that indicates whether the managed object has been inserted in a managed object context.
- [var isUpdated: Bool](nsmanagedobject/isupdated.md)
  A Boolean value that indicates whether the managed object has unsaved changes.
- [var isDeleted: Bool](nsmanagedobject/isdeleted.md)
  A Boolean value that indicates whether the managed object will be deleted during the next save.
- [var faultingState: Int](nsmanagedobject/faultingstate.md)
  The faulting state of the managed object.
- [func hasFault(forRelationshipNamed: String) -> Bool](nsmanagedobject/hasfault(forrelationshipnamed:).md)
  Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [var hasPersistentChangedValues: Bool](nsmanagedobject/haspersistentchangedvalues.md)
  A Boolean value that indicates whether the managed object has persistent changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/isfault)*