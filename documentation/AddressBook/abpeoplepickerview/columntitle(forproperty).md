# columnTitle(forProperty:)

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns the title of a custom property.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func columnTitle(forProperty property: String!) -> String!
```

```objc
- (NSString *) columnTitleForProperty:(NSString *) property;
```

#### Return Value

The title of the custom property.

## Parameters

- `property`: The property whose title will be returned.

## See Also

### Working with Properties in the Record List
- [func addProperty(String!)](./addproperty%28_%29.md)
  Adds a property to the group of properties whose values are shown in the record list.
- [var displayedProperty: String!](./displayedproperty.md)
  The property currently displayed in the record list.
- [func properties() -> [Any]!](./properties%28%29.md)
  Returns an array of the properties whose values are shown in the record list.
- [func removeProperty(String!)](./removeproperty%28_%29.md)
  Removes a property from the group of properties whose values are shown in the record list.
- [func setColumnTitle(String!, forProperty: String!)](./setcolumntitle%28_,forproperty%29.md)
  Sets the title displayed in the people picker for a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/columntitle(forproperty:))*