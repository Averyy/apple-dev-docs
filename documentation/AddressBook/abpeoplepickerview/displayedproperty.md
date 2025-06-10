# displayedProperty

**Framework**: Address Book  
**Kind**: property

The property currently displayed in the record list.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var displayedProperty: String! { get set }
```

## See Also

- [func addProperty(String!)](abpeoplepickerview/addproperty(_:).md)
  Adds a property to the group of properties whose values are shown in the record list.
- [func columnTitle(forProperty: String!) -> String!](abpeoplepickerview/columntitle(forproperty:).md)
  Returns the title of a custom property.
- [func properties() -> [Any]!](abpeoplepickerview/properties.md)
  Returns an array of the properties whose values are shown in the record list.
- [func removeProperty(String!)](abpeoplepickerview/removeproperty(_:).md)
  Removes a property from the group of properties whose values are shown in the record list.
- [func setColumnTitle(String!, forProperty: String!)](abpeoplepickerview/setcolumntitle(_:forproperty:).md)
  Sets the title displayed in the people picker for a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/displayedproperty)*