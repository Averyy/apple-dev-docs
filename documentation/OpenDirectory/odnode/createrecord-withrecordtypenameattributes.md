# createRecord(withRecordType:name:attributes:)

**Framework**: Open Directory  
**Kind**: method

Creates a record in a specified node with specified properties.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func createRecord(withRecordType inRecordType: String!, name inRecordName: String!, attributes inAttributes: [AnyHashable : Any]! = [:]) throws -> ODRecord
```

#### Return Value

The created record.

#### Discussion

The record is automatically assigned a UUID. This UUID can be overridden if one is specified in `inAttributes`.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecordType`: The record’s type.
- `inRecordName`: The record’s name.
- `inAttributes`: A dictionary of key-value pairs representing attributes for the record. Can be  .

## See Also

- [func record(withRecordType: String!, name: String!, attributes: Any!) throws -> ODRecord](odnode/record(withrecordtype:name:attributes:).md)
  Returns a record from the node with a specified type and name.
- [func supportedAttributes(forRecordType: String!) throws -> [Any]](odnode/supportedattributes(forrecordtype:).md)
  Returns an array of attribute types supported by the node’s records.
- [func supportedRecordTypes() throws -> [Any]](odnode/supportedrecordtypes.md)
  Returns an array of the record types supported by the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/createrecord(withrecordtype:name:attributes:))*