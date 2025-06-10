# supportedRecordTypes()

**Framework**: Open Directory  
**Kind**: method

Returns an array of the record types supported by the node.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
func supportedRecordTypes() throws -> [Any]
```

#### Return Value

An array of supported record types.

#### Discussion

If the node does not support checking for supported record types, all possible record types are returned.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

- [func createRecord(withRecordType: String!, name: String!, attributes: [AnyHashable : Any]!) throws -> ODRecord](odnode/createrecord(withrecordtype:name:attributes:).md)
  Creates a record in a specified node with specified properties.
- [func record(withRecordType: String!, name: String!, attributes: Any!) throws -> ODRecord](odnode/record(withrecordtype:name:attributes:).md)
  Returns a record from the node with a specified type and name.
- [func supportedAttributes(forRecordType: String!) throws -> [Any]](odnode/supportedattributes(forrecordtype:).md)
  Returns an array of attribute types supported by the node’s records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/supportedrecordtypes())*