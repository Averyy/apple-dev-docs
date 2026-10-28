# setValue(_:forProperty:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Sets the value of a given property for a record.

**Availability**:
- macOS

## Declaration

```swift
func setValue(_ value: Any!, forProperty property: String!) -> Bool
```

```objc
- (BOOL) setValue:(id) value forProperty:(NSString *) property;
```

## Return Value

`true` if the value was set successfully; otherwise, `false`.

## Discussion

The type of the value must match the property’s type (see [Property Types](../property_types.md) for a list of possible property types). If `property` is `nil` or if `value` is not of the correct type, this method raises an exception. If `property` is a multivalue list property, this method checks to see if the values in the multivalue list are the same type. If the multivalue list contains mixed types, the value will not be set successfully.

For a list of the available properties, see [Accessing Address Book Records](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AccessingData.html#//apple_ref/doc/uid/20001023) in [Address Book Programming Guide for Mac](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/AddressBook.html#//apple_ref/doc/uid/10000117i).

## Parameters

- `value`: The value to set for `property`.
- `property`: The property whose value will be set.

## See Also

### Retrieving and Setting Values
- [func removeValue(forProperty: String!) -> Bool](./removevalue%28forproperty%29.md)
  Removes the value for a given property.
- [func setValue(Any!, forProperty: String!, error: ()) throws](./setvalue%28_,forproperty,error%29.md)
  Sets the value of a given property for a record, returning error information.
- [func value(forProperty: String!) -> Any!](./value%28forproperty%29.md)
  Returns the value of a given property for a record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord-swift.class/setvalue(_:forproperty:))*