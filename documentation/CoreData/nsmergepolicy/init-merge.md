# init(merge:)

**Framework**: Core Data  
**Kind**: init

Returns a merge policy initialized with a given policy type.

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
init(merge ty: NSMergePolicyType)
```

#### Return Value

A merge policy initialized with a given policy type.

#### Discussion

If you override this method in a subclass, you should invoke the superclass’s implementation with the merge policy that is closest to the behavior you want.

- This will make it easier to use the superclass’s implementation of [`resolve(mergeConflicts:)`](nsmergepolicy/resolve(mergeconflicts:).md) and then customize the results.
- Due to the complexity of merging to-many relationships, this class is designed with the expectation that you call super as the base implementation.

## Parameters

- `ty`: A merge policy type.

## See Also

- [Core Data Model Versioning and Data Migration Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreDataVersioning/Articles/Introduction.html#//apple_ref/doc/uid/TP40004399)
- [var mergeType: NSMergePolicyType](nsmergepolicy/mergetype.md)
  The merge type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicy/init(merge:))*