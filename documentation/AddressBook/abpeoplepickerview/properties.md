# properties()

**Framework**: Address Book  
**Kind**: method

Returns an array of the properties whose values are shown in the record list.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func properties() -> [Any]!
```

#### Discussion

For additional information about properties see [`Using Property Lists`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AccessingData.html#//apple_ref/doc/uid/20001023-103048).

## See Also

- [func addProperty(String!)](abpeoplepickerview/addproperty(_:).md)
  Adds a property to the group of properties whose values are shown in the record list.
- [func columnTitle(forProperty: String!) -> String!](abpeoplepickerview/columntitle(forproperty:).md)
  Returns the title of a custom property.
- [var displayedProperty: String!](abpeoplepickerview/displayedproperty.md)
  The property currently displayed in the record list.
- [func removeProperty(String!)](abpeoplepickerview/removeproperty(_:).md)
  Removes a property from the group of properties whose values are shown in the record list.
- [func setColumnTitle(String!, forProperty: String!)](abpeoplepickerview/setcolumntitle(_:forproperty:).md)
  Sets the title displayed in the people picker for a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/properties())*