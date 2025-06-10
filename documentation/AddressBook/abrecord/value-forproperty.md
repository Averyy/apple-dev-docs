# value(forProperty:)

**Framework**: Address Book  
**Kind**: method

Returns the value of a given property for a record.

**Availability**:
- macOS ?+

## Declaration

```swift
func value(forProperty property: String!) -> Any!
```

#### Return Value

The value of the given property.

#### Discussion

The type of the value depends on the property type (see [`Property Types`](property_types.md) for a list of possible property types). Note that the returned value is always of an immutable type (for example, an `NSString` type, not an `NSMutableString` type, is returned).

If `property` is `nil`, this method raises an exception. If `property` is invalid, this method returns `nil`.

For a list of the available properties, see [`Accessing Address Book Records`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AccessingData.html#//apple_ref/doc/uid/20001023) in [`Address Book Programming Guide for Mac`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/AddressBook.html#//apple_ref/doc/uid/10000117i).

## Parameters

- `property`: The property whose value will be returned.

## See Also

- [func removeValue(forProperty: String!) -> Bool](abrecord/removevalue(forproperty:).md)
  Removes the value for a given property.
- [func setValue(Any!, forProperty: String!) -> Bool](abrecord/setvalue(_:forproperty:).md)
  Sets the value of a given property for a record.
- [func setValue(Any!, forProperty: String!, error: ()) throws](abrecord/setvalue(_:forproperty:error:).md)
  Sets the value of a given property for a record, returning error information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord/value(forproperty:))*