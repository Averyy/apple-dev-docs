# fetch(with:merge:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Subclasses should override this method to customize a fetch request, for example to specify fetch limits.

**Availability**:
- macOS

## Declaration

```swift
func fetch(with fetchRequest: NSFetchRequest<any NSFetchRequestResult>?, merge: Bool) throws
```

```objc
- (BOOL) fetchWithRequest:(NSFetchRequest *) fetchRequest merge:(BOOL) merge error:(NSError **) error;
```

## Discussion

This method performs a number of actions that you cannot reproduce. To customize this method, you should therefore create your own fetch request and then invoke `super`’s implementation with the new fetch request.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `fetchRequest`: The fetch request to use for the fetch. Pass `nil` to use the default fetch request.
- `merge`: If [`true`](../../Swift/true.md), the receiver merges the existing content with the fetch result, otherwise the receiver replaces the entire content with the fetch result.

## See Also

### Core Data support
- [var entityName: String?](./entityname.md)
  The entity name used by the receiver to create new objects.
- [func fetch(Any?)](./fetch%28_%29.md)
  Causes the receiver to fetch the data objects specified by the entity name and fetch predicate.
- [var usesLazyFetching: Bool](./useslazyfetching.md)
  A Boolean that indicates whether the receiver uses lazy fetching.
- [func defaultFetchRequest() -> NSFetchRequest<any NSFetchRequestResult>](./defaultfetchrequest%28%29.md)
  Returns the default fetch request used by the receiver.
- [var fetchPredicate: NSPredicate?](./fetchpredicate.md)
  The receiver’s fetch predicate.
- [var managedObjectContext: NSManagedObjectContext?](./managedobjectcontext.md)
  The receiver’s managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsobjectcontroller/fetch(with:merge:))*