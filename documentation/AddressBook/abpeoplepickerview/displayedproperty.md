# displayedProperty

**Framework**: Address Book  
**Kind**: property  
**Role**: Instance Property

The property currently displayed in the record list.

**Availability**:
- macOS 10.3+

## Declaration

```swift
var displayedProperty: String! { get set }
```

```objc
@property (nonatomic, retain) NSString * displayedProperty;
```

## See Also

### Working with Properties in the Record List
- [func addProperty(String!)](./addproperty%28_%29.md)
  Adds a property to the group of properties whose values are shown in the record list.
- [func columnTitle(forProperty: String!) -> String!](./columntitle%28forproperty%29.md)
  Returns the title of a custom property.
- [func properties() -> [Any]!](./properties%28%29.md)
  Returns an array of the properties whose values are shown in the record list.
- [func removeProperty(String!)](./removeproperty%28_%29.md)
  Removes a property from the group of properties whose values are shown in the record list.
- [func setColumnTitle(String!, forProperty: String!)](./setcolumntitle%28_,forproperty%29.md)
  Sets the title displayed in the people picker for a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abpeoplepickerview/displayedproperty)*