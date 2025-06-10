# supportedAttributes(forRecordType:)

**Framework**: Open Directory  
**Kind**: method

Returns an array of attribute types supported by the node’s records.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func supportedAttributes(forRecordType inRecordType: String!) throws -> [Any]
```

#### Return Value

An array of supported attribute types.

#### Discussion

If `inRecordType` is `nil`, this function returns all attribute types supported by all record types of the node; otherwise, only attribute types specific to `inRecordType` are returned.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecordType`: The record type to list supported attribute types for. Can be  .

## See Also

- [func createRecord(withRecordType: String!, name: String!, attributes: [AnyHashable : Any]!) throws -> ODRecord](odnode/createrecord(withrecordtype:name:attributes:).md)
  Creates a record in a specified node with specified properties.
- [func record(withRecordType: String!, name: String!, attributes: Any!) throws -> ODRecord](odnode/record(withrecordtype:name:attributes:).md)
  Returns a record from the node with a specified type and name.
- [func supportedRecordTypes() throws -> [Any]](odnode/supportedrecordtypes.md)
  Returns an array of the record types supported by the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/supportedattributes(forrecordtype:))*