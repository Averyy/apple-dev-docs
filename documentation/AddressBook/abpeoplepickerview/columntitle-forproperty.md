# columnTitle(forProperty:)

**Framework**: Address Book  
**Kind**: method

Returns the title of a custom property.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func columnTitle(forProperty property: String!) -> String!
```

#### Return Value

The title of the custom property.

## Parameters

- `property`: The property whose title will be returned.

## See Also

- [func addProperty(String!)](abpeoplepickerview/addproperty(_:).md)
  Adds a property to the group of properties whose values are shown in the record list.
- [var displayedProperty: String!](abpeoplepickerview/displayedproperty.md)
  The property currently displayed in the record list.
- [func properties() -> [Any]!](abpeoplepickerview/properties.md)
  Returns an array of the properties whose values are shown in the record list.
- [func removeProperty(String!)](abpeoplepickerview/removeproperty(_:).md)
  Removes a property from the group of properties whose values are shown in the record list.
- [func setColumnTitle(String!, forProperty: String!)](abpeoplepickerview/setcolumntitle(_:forproperty:).md)
  Sets the title displayed in the people picker for a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/columntitle(forproperty:))*