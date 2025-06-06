# save()

**Framework**: Core Data  
**Kind**: method

Attempts to commit unsaved changes to registered objects to the context’s parent store.

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
func save() throws
```

## Mentions

- [Accessing data when the store changes](accessing-data-when-the-store-changes.md)

#### Discussion

If there were multiple errors (for example several edited objects had validation failures) the description of `NSError` returned indicates that there were multiple errors, and its userInfo dictionary contains the key `NSDetailedErrors`. The value associated with the `NSDetailedErrors` key is an array that contains the individual `NSError` objects.

If a context’s parent store is a persistent store coordinator, then changes are committed to the external store. If a context’s parent store is another managed object context, then [`save()`](nsmanagedobjectcontext/save().md) only updates managed objects in that parent store. To commit changes to the external store, you must save changes in the chain of contexts up to and including the context whose parent is the persistent store coordinator.

> ❗ **Important**:  Always verify that the context has uncommitted changes (using the [`hasChanges`](nsmanagedobjectcontext/haschanges.md) property) before invoking the `save:` method. Otherwise, Core Data may perform unnecessary work.

 Always verify that the context has uncommitted changes (using the [`hasChanges`](nsmanagedobjectcontext/haschanges.md) property) before invoking the `save:` method. Otherwise, Core Data may perform unnecessary work.

## See Also

- [var hasChanges: Bool](nsmanagedobjectcontext/haschanges.md)
  A Boolean value that indicates whether the context has uncommitted changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/save())*