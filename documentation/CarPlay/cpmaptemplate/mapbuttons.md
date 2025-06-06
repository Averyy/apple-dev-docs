# mapButtons

**Framework**: CarPlay  
**Kind**: property

An array of map buttons on the trailing bottom corner of the map template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var mapButtons: [CPMapButton] { get set }
```

#### Discussion

When the array contains more than three buttons, the map template displays only the first three, ignoring the remaining buttons.

## See Also

- [class CPMapButton](cpmapbutton.md)
  A button that represents an action that a map template displays on the CarPlay screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/mapbuttons)*