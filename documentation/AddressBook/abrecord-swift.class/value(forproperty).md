# value(forProperty:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the value of a given property for a record.

**Availability**:
- macOS

## Declaration

```swift
func value(forProperty property: String!) -> Any!
```

```objc
- (id) valueForProperty:(NSString *) property;
```

## Return Value

The value of the given property.

## Discussion

The type of the value depends on the property type (see [Property Types](../property_types.md) for a list of possible property types). Note that the returned value is always of an immutable type (for example, an `NSString` type, not an `NSMutableString` type, is returned).

If `property` is `nil`, this method raises an exception. If `property` is invalid, this method returns `nil`.

For a list of the available properties, see [Accessing Address Book Records](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AccessingData.html#//apple_ref/doc/uid/20001023) in [Address Book Programming Guide for Mac](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/AddressBook.html#//apple_ref/doc/uid/10000117i).

## Parameters

- `property`: The property whose value will be returned.

## See Also

### Retrieving and Setting Values
- [func removeValue(forProperty: String!) -> Bool](./removevalue%28forproperty%29.md)
  Removes the value for a given property.
- [func setValue(Any!, forProperty: String!) -> Bool](./setvalue%28_,forproperty%29.md)
  Sets the value of a given property for a record.
- [func setValue(Any!, forProperty: String!, error: ()) throws](./setvalue%28_,forproperty,error%29.md)
  Sets the value of a given property for a record, returning error information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord-swift.class/value(forproperty:))*