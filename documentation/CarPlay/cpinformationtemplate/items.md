# items

**Framework**: CarPlay  
**Kind**: property

The items that the template displays.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
var items: [CPInformationItem] { get set }
```

#### Discussion

Assign a new array to this property to update the items that the template displays. The template can display 10 items maximum. If the array contains more items, the template uses only the first 10.

## See Also

- [class CPInformationItem](cpinformationitem.md)
  A data object that provides content for an information template.
- [class CPInformationRatingItem](cpinformationratingitem.md)
  A data object that provides rated content for an information template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpinformationtemplate/items)*