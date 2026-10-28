# supportedAttributes(forRecordType:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Returns an array of attribute types supported by the node’s records.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func supportedAttributes(forRecordType inRecordType: String!) throws -> [Any]
```

```objc
- (NSArray *) supportedAttributesForRecordType:(ODRecordType) inRecordType error:(NSError **) outError;
```

## Return Value

An array of supported attribute types.

## Discussion

If `inRecordType` is `nil`, this function returns all attribute types supported by all record types of the node; otherwise, only attribute types specific to `inRecordType` are returned.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecordType`: The record type to list supported attribute types for. Can be `nil`.

## See Also

### Managing Node Records
- [func createRecord(withRecordType: String!, name: String!, attributes: [AnyHashable : Any]!) throws -> ODRecord](./createrecord%28withrecordtype,name,attributes%29.md)
  Creates a record in a specified node with specified properties.
- [func record(withRecordType: String!, name: String!, attributes: Any!) throws -> ODRecord](./record%28withrecordtype,name,attributes%29.md)
  Returns a record from the node with a specified type and name.
- [func supportedRecordTypes() throws -> [Any]](./supportedrecordtypes%28%29.md)
  Returns an array of the record types supported by the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/supportedattributes(forrecordtype:))*