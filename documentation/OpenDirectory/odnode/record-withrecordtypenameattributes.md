# record(withRecordType:name:attributes:)

**Framework**: Opendirectory  
**Kind**: method

Returns a record from the node with a specified type and name.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func record(withRecordType inRecordType: String!, name inRecordName: String!, attributes inAttributes: Any!) throws -> ODRecord
```

#### Return Value

The requested record.

#### Discussion

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecordType`: The type of the record.
- `inRecordName`: The name of the record.
- `inAttributes`: An array of record attributes to be cached before the record is returned. Can be  .

## See Also

- [func createRecord(withRecordType: String!, name: String!, attributes: [AnyHashable : Any]!) throws -> ODRecord](odnode/createrecord(withrecordtype:name:attributes:).md)
  Creates a record in a specified node with specified properties.
- [func supportedAttributes(forRecordType: String!) throws -> [Any]](odnode/supportedattributes(forrecordtype:).md)
  Returns an array of attribute types supported by the node’s records.
- [func supportedRecordTypes() throws -> [Any]](odnode/supportedrecordtypes.md)
  Returns an array of the record types supported by the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/record(withrecordtype:name:attributes:))*