# addProperty(_:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Adds a property to the group of properties whose values are shown in the record list.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func addProperty(_ property: String!)
```

```objc
- (void) addProperty:(NSString *) property;
```

#### Discussion

For additional information about properties see Constants.

## Parameters

- `property`: The property to add.

## See Also

### Working with Properties in the Record List
- [func columnTitle(forProperty: String!) -> String!](./columntitle%28forproperty%29.md)
  Returns the title of a custom property.
- [var displayedProperty: String!](./displayedproperty.md)
  The property currently displayed in the record list.
- [func properties() -> [Any]!](./properties%28%29.md)
  Returns an array of the properties whose values are shown in the record list.
- [func removeProperty(String!)](./removeproperty%28_%29.md)
  Removes a property from the group of properties whose values are shown in the record list.
- [func setColumnTitle(String!, forProperty: String!)](./setcolumntitle%28_,forproperty%29.md)
  Sets the title displayed in the people picker for a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/addproperty(_:))*