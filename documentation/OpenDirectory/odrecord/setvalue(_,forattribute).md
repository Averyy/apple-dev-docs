# setValue(_:forAttribute:)

**Framework**: Open Directory  
**Kind**: method  
**Role**: Instance Method

Sets the values of an attribute of the record.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
func setValue(_ inValueOrValues: Any!, forAttribute inAttribute: String!) throws
```

```objc
- (BOOL) setValue:(id) inValueOrValues forAttribute:(ODAttributeType) inAttribute error:(NSError **) outError;
```

## Discussion

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `inValueOrValues`: The value or values. Can be of type `NSString` or `NSData`, or an `NSArray` with elements of both types.
- `inAttribute`: The attribute.

## See Also

### Managing Record Attributes
- [func addValue(Any!, toAttribute: String!) throws](./addvalue%28_,toattribute%29.md)
  Adds a value to an attribute of the record.
- [func recordDetails(forAttributes: [Any]!) throws -> [AnyHashable : Any]](./recorddetails%28forattributes%29.md)
  Returns a dictionary of attributes with their respective values.
- [var recordName: String!](./recordname.md)
  The official name of the record.
- [var recordType: String!](./recordtype.md)
  The record’s type.
- [func removeValues(forAttribute: String!) throws](./removevalues%28forattribute%29.md)
  Removes all values from an attribute of the record.
- [func removeValue(Any!, fromAttribute: String!) throws](./removevalue%28_,fromattribute%29.md)
  Removes a value from an attribute of the record.
- [func synchronize() throws](./synchronize%28%29.md)
  Synchronizes the record from the directory to get current data and commit changes.
- [func values(forAttribute: String!) throws -> [Any]](./values%28forattribute%29.md)
  Returns the values of an attribute of the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/setvalue(_:forattribute:))*