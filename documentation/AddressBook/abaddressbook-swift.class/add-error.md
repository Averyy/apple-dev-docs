# add(_:error:)

**Framework**: Address Book  
**Kind**: method

Adds an `ABPerson` or `ABGroup` record to the Address Book database.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func add(_ record: ABRecord!, error: ()) throws
```

#### Discussion

If the `record` argument is `nil`, this method raises an exception. Your changes are not committed until you call the [`save()`](abaddressbook-swift.class/save().md) method.

It is more efficient to use the  [`ABRecord`](abrecord-swift.class.md) method [`init(addressBook:)`](abrecord-swift.class/init(addressbook:).md) when possible.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `record`: The record to add.
- `error`: A pointer to an error object that is set to an   instance if an error occurs.

## See Also

- [func add(ABRecord!) -> Bool](abaddressbook-swift.class/add(_:).md)
  Adds an `ABPerson` or `ABGroup` record to the Address Book database.
- [func remove(ABRecord!, error: ()) throws](abaddressbook-swift.class/remove(_:error:).md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.
- [func remove(ABRecord!) -> Bool](abaddressbook-swift.class/remove(_:).md)
  Removes an `ABPerson` or `ABGroup` record from the Address Book database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abaddressbook-swift.class/add(_:error:))*