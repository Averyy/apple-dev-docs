# removeValue(forProperty:)

**Framework**: Address Book  
**Kind**: method

Removes the value for a given property.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeValue(forProperty property: String!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the value is removed successfully; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

When you next call [`value(forProperty:)`](abrecord/value(forproperty:).md) on that property, it returns `nil`.

If property is `nil`, this method raises an exception.

For a list of the available properties, see [`Accessing Address Book Records`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AccessingData.html#//apple_ref/doc/uid/20001023) in [`Address Book Programming Guide for Mac`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/AddressBook.html#//apple_ref/doc/uid/10000117i).

## Parameters

- `property`: The property whose value will be removed.

## See Also

- [func setValue(Any!, forProperty: String!) -> Bool](abrecord/setvalue(_:forproperty:).md)
  Sets the value of a given property for a record.
- [func setValue(Any!, forProperty: String!, error: ()) throws](abrecord/setvalue(_:forproperty:error:).md)
  Sets the value of a given property for a record, returning error information.
- [func value(forProperty: String!) -> Any!](abrecord/value(forproperty:).md)
  Returns the value of a given property for a record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord/removevalue(forproperty:))*