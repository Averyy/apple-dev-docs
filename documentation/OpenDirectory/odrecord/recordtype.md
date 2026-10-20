# recordType

**Framework**: Open Directory  
**Kind**: property  
**Role**: Instance Property

The record’s type.

**Availability**:
- Mac Catalyst
- macOS 10.6+

## Declaration

```swift
var recordType: String! { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * recordType;
```

## See Also

### Managing Record Attributes
- [func addValue(Any!, toAttribute: String!) throws](./addvalue%28_,toattribute%29.md)
  Adds a value to an attribute of the record.
- [func recordDetails(forAttributes: [Any]!) throws -> [AnyHashable : Any]](./recorddetails%28forattributes%29.md)
  Returns a dictionary of attributes with their respective values.
- [var recordName: String!](./recordname.md)
  The official name of the record.
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

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/recordtype)*