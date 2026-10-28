# faultingState

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The faulting state of the managed object.

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
var faultingState: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger faultingState;
```

## Return Value

`0` if the object is fully initialized as a managed object and not transitioning to or from another state, otherwise some other value.

## Discussion

`0` if the object is fully initialized as a managed object and not transitioning to or from another state, otherwise some other value. This property allows you to determine if an object is in a transitional phase when receiving a key-value observing change notification.

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
- [func hasFault(forRelationshipNamed: String) -> Bool](./hasfault%28forrelationshipnamed%29.md)
  Returns a Boolean value that indicates whether the relationship for a given key is a fault.
- [var hasPersistentChangedValues: Bool](./haspersistentchangedvalues.md)
  A Boolean value that indicates whether the managed object has persistent changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/faultingstate)*