# addMemberRecord(_:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Adds a member record to this group record.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func addMemberRecord(_ inRecord: ODRecord!) throws
```

```objc
- (BOOL) addMemberRecord:(ODRecord *) inRecord error:(NSError **) outError;
```

## Discussion

This method produces an error if this record is not a group record, or if `inRecord` is not an appropriate type.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecord`: The member record to add.

## See Also

### Managing Group Records
- [func isMemberRecord(ODRecord!) throws](./ismemberrecord%28_%29.md)
  Determines whether a given record is a member of this group record.
- [func removeMemberRecord(ODRecord!) throws](./removememberrecord%28_%29.md)
  Removes a record as a member of this group record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/addmemberrecord(_:))*