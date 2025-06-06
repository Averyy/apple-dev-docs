# recordDetails(forAttributes:)

**Framework**: Open Directory  
**Kind**: method

Returns a dictionary of attributes with their respective values.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func recordDetails(forAttributes inAttributes: [Any]!) throws -> [AnyHashable : Any]
```

#### Return Value

A dictionary of the attributes in `inAttributes` with their respective values.

#### Discussion

If `inAttributes` is `nil`, all currently retrieved attributes are returned.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inAttributes`: An array of attributes. Can be  .

## See Also

- [func addValue(Any!, toAttribute: String!) throws](odrecord/addvalue(_:toattribute:).md)
  Adds a value to an attribute of the record.
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
- [func synchronize() throws](odrecord/synchronize.md)
  Synchronizes the record from the directory to get current data and commit changes.
- [func values(forAttribute: String!) throws -> [Any]](odrecord/values(forattribute:).md)
  Returns the values of an attribute of the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/recorddetails(forattributes:))*