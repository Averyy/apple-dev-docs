# registerStyleName(_:type:inherited:)

**Framework**: TVMLKit  
**Kind**: method

Creates a new style property of the indicated type.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class func registerStyleName(_ styleName: String, type: TVViewElementStyleType, inherited: Bool)
```

## Parameters

- `styleName`: The name used to identify the style.
- `type`: The element style type as specified by  .
- `inherited`: Boolean indicating whether the style is able to be inherited by other styles.

## See Also

- [enum TVViewElementStyleType](tvviewelementstyletype.md)
  Describes the different style types for an element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvstylefactory/registerstylename(_:type:inherited:))*