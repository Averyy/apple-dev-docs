# properties()

**Framework**: Address Book  
**Kind**: method  
**Role**: Instance Method

Returns an array of the properties whose values are shown in the record list.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func properties() -> [Any]!
```

```objc
- (NSArray *) properties;
```

#### Discussion

For additional information about properties see [Using Property Lists](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/AddressBook/Tasks/AccessingData.html#//apple_ref/doc/uid/20001023-103048).

## See Also

### Working with Properties in the Record List
- [func addProperty(String!)](./addproperty%28_%29.md)
  Adds a property to the group of properties whose values are shown in the record list.
- [func columnTitle(forProperty: String!) -> String!](./columntitle%28forproperty%29.md)
  Returns the title of a custom property.
- [var displayedProperty: String!](./displayedproperty.md)
  The property currently displayed in the record list.
- [func removeProperty(String!)](./removeproperty%28_%29.md)
  Removes a property from the group of properties whose values are shown in the record list.
- [func setColumnTitle(String!, forProperty: String!)](./setcolumntitle%28_,forproperty%29.md)
  Sets the title displayed in the people picker for a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/properties())*