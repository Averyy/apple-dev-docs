# delete()

**Framework**: Open Directory  
**Kind**: method

Deletes the record from its node and invalidates it.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func delete() throws
```

#### Discussion

The record should be released after this method is called.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/delete())*