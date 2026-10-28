# remove(_:error:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Removes an `ABPerson` or `ABGroup` record from the Address Book database.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func remove(_ record: ABRecord!, error: ()) throws
```

```objc
- (BOOL) removeRecord:(ABRecord *) record error:(NSError **) error;
```

## Discussion

If `record` is `nil`, this method raises an exception. Your changes are not committed until you call the [`save()`](./save%28%29.md) method.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `record`: The record to be removed.
- `error`: A pointer to an error object that is set to an `NSError` instance if an error occurs.

## See Also

### Adding and Removing Records
- [func add(ABRecord!, error: ()) throws](./add%28_,error%29.md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func add(ABRecord!) -> Bool](./add%28_%29.md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func remove(ABRecord!) -> Bool](./remove%28_%29.md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/remove(_:error:))*