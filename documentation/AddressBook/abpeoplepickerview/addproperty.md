# addProperty(_:)

**Framework**: Address Book  
**Kind**: method

Adds a property to the group of properties whose values are shown in the record list.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func addProperty(_ property: String!)
```

#### Discussion

For additional information about properties see Constants.

## Parameters

- `property`: The property to add.

## See Also

- [func columnTitle(forProperty: String!) -> String!](abpeoplepickerview/columntitle(forproperty:).md)
  Returns the title of a custom property.
- [var displayedProperty: String!](abpeoplepickerview/displayedproperty.md)
  The property currently displayed in the record list.
- [func properties() -> [Any]!](abpeoplepickerview/properties.md)
  Returns an array of the properties whose values are shown in the record list.
- [func removeProperty(String!)](abpeoplepickerview/removeproperty(_:).md)
  Removes a property from the group of properties whose values are shown in the record list.
- [func setColumnTitle(String!, forProperty: String!)](abpeoplepickerview/setcolumntitle(_:forproperty:).md)
  Sets the title displayed in the people picker for a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/addproperty(_:))*