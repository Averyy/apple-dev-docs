# removeValue(forProperty:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Removes the value for a given property.

**Availability**:
- macOS

## Declaration

```swift
func removeValue(forProperty property: String!) -> Bool
```

```objc
- (BOOL) removeValueForProperty:(NSString *) property;
```

## Return Value

[`true`](../../Swift/true.md) if the value is removed successfully; otherwise, [`false`](../../Swift/false.md).

## Discussion

When you next call [`value(forProperty:)`](./value%28forproperty%29.md) on that property, it returns `nil`.

If property is `nil`, this method raises an exception.

For a list of the available properties, see [Accessing Address Book Records](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AccessingData.html#//apple_ref/doc/uid/20001023) in [Address Book Programming Guide for Mac](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/AddressBook.html#//apple_ref/doc/uid/10000117i).

## Parameters

- `property`: The property whose value will be removed.

## See Also

### Retrieving and Setting Values
- [func setValue(Any!, forProperty: String!) -> Bool](./setvalue%28_,forproperty%29.md)
  Sets the value of a given property for a record.
- [func setValue(Any!, forProperty: String!, error: ()) throws](./setvalue%28_,forproperty,error%29.md)
  Sets the value of a given property for a record, returning error information.
- [func value(forProperty: String!) -> Any!](./value%28forproperty%29.md)
  Returns the value of a given property for a record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord-swift.class/removevalue(forproperty:))*