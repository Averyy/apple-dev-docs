# hasPersistentChangedValues

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the managed object has persistent changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var hasPersistentChangedValues: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL hasPersistentChangedValues;
```

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
- [func hasFault(forRelationshipNamed: String) -> Bool](./hasfault%28forrelationshipnamed%29.md)
  Returns a Boolean value that indicates whether the relationship for a given key is a fault.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/haspersistentchangedvalues)*