# createRecord(withRecordType:name:attributes:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Creates a record in a specified node with specified properties.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func createRecord(withRecordType inRecordType: String!, name inRecordName: String!, attributes inAttributes: [AnyHashable : Any]! = [:]) throws -> ODRecord
```

```objc
- (ODRecord *) createRecordWithRecordType:(ODRecordType) inRecordType name:(NSString *) inRecordName attributes:(NSDictionary *) inAttributes error:(NSError **) outError;
```

#### Return Value

The created record.

#### Discussion

The record is automatically assigned a UUID. This UUID can be overridden if one is specified in `inAttributes`.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inRecordType`: The record’s type.
- `inRecordName`: The record’s name.
- `inAttributes`: A dictionary of key-value pairs representing attributes for the record. Can be `nil`.

## See Also

### Managing Node Records
- [func record(withRecordType: String!, name: String!, attributes: Any!) throws -> ODRecord](./record%28withrecordtype,name,attributes%29.md)
  Returns a record from the node with a specified type and name.
- [func supportedAttributes(forRecordType: String!) throws -> [Any]](./supportedattributes%28forrecordtype%29.md)
  Returns an array of attribute types supported by the node’s records.
- [func supportedRecordTypes() throws -> [Any]](./supportedrecordtypes%28%29.md)
  Returns an array of the record types supported by the node.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odnode/createrecord(withrecordtype:name:attributes:))*