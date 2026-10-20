# recordDetails(forAttributes:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Returns a dictionary of attributes with their respective values.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func recordDetails(forAttributes inAttributes: [Any]!) throws -> [AnyHashable : Any]
```

```objc
- (NSDictionary *) recordDetailsForAttributes:(NSArray *) inAttributes error:(NSError **) outError;
```

#### Return Value

A dictionary of the attributes in `inAttributes` with their respective values.

#### Discussion

If `inAttributes` is `nil`, all currently retrieved attributes are returned.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inAttributes`: An array of attributes. Can be `nil`.

## See Also

### Managing Record Attributes
- [func addValue(Any!, toAttribute: String!) throws](./addvalue%28_,toattribute%29.md)
  Adds a value to an attribute of the record.
- [var recordName: String!](./recordname.md)
  The official name of the record.
- [var recordType: String!](./recordtype.md)
  The record’s type.
- [func removeValues(forAttribute: String!) throws](./removevalues%28forattribute%29.md)
  Removes all values from an attribute of the record.
- [func removeValue(Any!, fromAttribute: String!) throws](./removevalue%28_,fromattribute%29.md)
  Removes a value from an attribute of the record.
- [func setValue(Any!, forAttribute: String!) throws](./setvalue%28_,forattribute%29.md)
  Sets the values of an attribute of the record.
- [func synchronize() throws](./synchronize%28%29.md)
  Synchronizes the record from the directory to get current data and commit changes.
- [func values(forAttribute: String!) throws -> [Any]](./values%28forattribute%29.md)
  Returns the values of an attribute of the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/recorddetails(forattributes:))*