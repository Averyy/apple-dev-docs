# removeMemberRecord(_:)

**Framework**: Open Directory  
**Kind**: method

Removes a record as a member of this group record.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func removeMemberRecord(_ inRecord: ODRecord!) throws
```

#### Discussion

This method produces an error if this record is not a group record, or if `inRecord` is not an appropriate type.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecord`: The member record.

## See Also

- [func addMemberRecord(ODRecord!) throws](odrecord/addmemberrecord(_:).md)
  Adds a member record to this group record.
- [func isMemberRecord(ODRecord!) throws](odrecord/ismemberrecord(_:).md)
  Determines whether a given record is a member of this group record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/removememberrecord(_:))*