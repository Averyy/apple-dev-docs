# remove(_:error:)

**Framework**: Address Book  
**Kind**: method

Removes an `ABPerson` or `ABGroup` record from the Address Book database.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func remove(_ record: ABRecord!, error: ()) throws
```

#### Discussion

If `record` is `nil`, this method raises an exception. Your changes are not committed until you call the [`save()`](abaddressbook/save().md) method.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `record`: The record to be removed.
- `error`: A pointer to an error object that is set to an   instance if an error occurs.

## See Also

- [func add(ABRecord!, error: ()) throws](abaddressbook/add(_:error:).md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func add(ABRecord!) -> Bool](abaddressbook/add(_:).md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func remove(ABRecord!) -> Bool](abaddressbook/remove(_:).md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook/remove(_:error:))*