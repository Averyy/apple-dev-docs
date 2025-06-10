# setColumnTitle(_:forProperty:)

**Framework**: Address Book  
**Kind**: method

Sets the title displayed in the people picker for a property.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func setColumnTitle(_ title: String!, forProperty property: String!)
```

## Parameters

- `title`: The title to be set.
- `property`: The property being titled.

## See Also

- [func addProperty(String!)](abpeoplepickerview/addproperty(_:).md)
  Adds a property to the group of properties whose values are shown in the record list.
- [func columnTitle(forProperty: String!) -> String!](abpeoplepickerview/columntitle(forproperty:).md)
  Returns the title of a custom property.
- [var displayedProperty: String!](abpeoplepickerview/displayedproperty.md)
  The property currently displayed in the record list.
- [func properties() -> [Any]!](abpeoplepickerview/properties.md)
  Returns an array of the properties whose values are shown in the record list.
- [func removeProperty(String!)](abpeoplepickerview/removeproperty(_:).md)
  Removes a property from the group of properties whose values are shown in the record list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/setcolumntitle(_:forproperty:))*