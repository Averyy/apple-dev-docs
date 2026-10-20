# mapButtons

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An array of map buttons on the trailing bottom corner of the map template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var mapButtons: [CPMapButton] { get set }
```

```objc
@property (nonatomic, strong) NSArray<CPMapButton *> * mapButtons;
```

#### Discussion

When the array contains more than three buttons, the map template displays only the first three, ignoring the remaining buttons.

## See Also

### Managing Map Buttons
- [class CPMapButton](../cpmapbutton.md)
  A button that represents an action that a map template displays on the CarPlay screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/mapbuttons)*