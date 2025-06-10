# synchronize()

**Framework**: Open Directory  
**Kind**: method

Synchronizes the record from the directory to get current data and commit changes.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func synchronize() throws
```

#### Discussion

This method only fetches those attributes that have been fetched before.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

- [func addValue(Any!, toAttribute: String!) throws](odrecord/addvalue(_:toattribute:).md)
  Adds a value to an attribute of the record.
- [func recordDetails(forAttributes: [Any]!) throws -> [AnyHashable : Any]](odrecord/recorddetails(forattributes:).md)
  Returns a dictionary of attributes with their respective values.
- [var recordName: String!](odrecord/recordname.md)
  The official name of the record.
- [var recordType: String!](odrecord/recordtype.md)
  The record’s type.
- [func removeValues(forAttribute: String!) throws](odrecord/removevalues(forattribute:).md)
  Removes all values from an attribute of the record.
- [func removeValue(Any!, fromAttribute: String!) throws](odrecord/removevalue(_:fromattribute:).md)
  Removes a value from an attribute of the record.
- [func setValue(Any!, forAttribute: String!) throws](odrecord/setvalue(_:forattribute:).md)
  Sets the values of an attribute of the record.
- [func values(forAttribute: String!) throws -> [Any]](odrecord/values(forattribute:).md)
  Returns the values of an attribute of the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/synchronize())*