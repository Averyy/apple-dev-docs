# recordType

**Framework**: Open Directory  
**Kind**: property

The record’s type.

**Availability**:
- Mac Catalyst ?+
- macOS 10.6+

## Declaration

```swift
var recordType: String! { get }
```

## See Also

- [func addValue(Any!, toAttribute: String!) throws](odrecord/addvalue(_:toattribute:).md)
  Adds a value to an attribute of the record.
- [func recordDetails(forAttributes: [Any]!) throws -> [AnyHashable : Any]](odrecord/recorddetails(forattributes:).md)
  Returns a dictionary of attributes with their respective values.
- [var recordName: String!](odrecord/recordname.md)
  The official name of the record.
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

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/odrecord/recordtype)*