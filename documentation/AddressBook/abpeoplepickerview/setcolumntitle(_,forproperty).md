# setColumnTitle(_:forProperty:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Sets the title displayed in the people picker for a property.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func setColumnTitle(_ title: String!, forProperty property: String!)
```

```objc
- (void) setColumnTitle:(NSString *) title forProperty:(NSString *) property;
```

## Parameters

- `title`: The title to be set.
- `property`: The property being titled.

## See Also

### Working with Properties in the Record List
- [func addProperty(String!)](./addproperty%28_%29.md)
  Adds a property to the group of properties whose values are shown in the record list.
- [func columnTitle(forProperty: String!) -> String!](./columntitle%28forproperty%29.md)
  Returns the title of a custom property.
- [var displayedProperty: String!](./displayedproperty.md)
  The property currently displayed in the record list.
- [func properties() -> [Any]!](./properties%28%29.md)
  Returns an array of the properties whose values are shown in the record list.
- [func removeProperty(String!)](./removeproperty%28_%29.md)
  Removes a property from the group of properties whose values are shown in the record list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/setcolumntitle(_:forproperty:))*