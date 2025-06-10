# setValue(_:forProperty:error:)

**Framework**: Address Book  
**Kind**: method

Sets the value of a given property for a record, returning error information.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setValue(_ value: Any!, forProperty property: String!, error: ()) throws
```

#### Discussion

The type of the value must match the property’s type (see [`Property Types`](property_types.md) for a list of possible property types). If `property` is `nil` or if `value` is not of the correct type, this method raises an exception. If `property` is a multivalue list property, this method checks to see if the values in the multivalue list are the same type. If the multivalue list contains mixed types, the value will not be set successfully.

For a list of the available properties, see [`Accessing Address Book Records`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AccessingData.html#//apple_ref/doc/uid/20001023) in [`Address Book Programming Guide for Mac`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/AddressBook.html#//apple_ref/doc/uid/10000117i).

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `value`: The value to set for  .
- `property`: The property whose value will be set.
- `error`: A pointer to an error object that is set to an   instance if an error occurs.

## See Also

- [func removeValue(forProperty: String!) -> Bool](abrecord/removevalue(forproperty:).md)
  Removes the value for a given property.
- [func setValue(Any!, forProperty: String!) -> Bool](abrecord/setvalue(_:forproperty:).md)
  Sets the value of a given property for a record.
- [func value(forProperty: String!) -> Any!](abrecord/value(forproperty:).md)
  Returns the value of a given property for a record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abrecord/setvalue(_:forproperty:error:))*