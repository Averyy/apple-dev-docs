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

## Discussion

When the array contains more than three buttons, the map template displays only the first three, ignoring the remaining buttons.

## See Also

### Configuring the map template
- [var automaticallyHidesNavigationBar: Bool](./automaticallyhidesnavigationbar.md)
  A Boolean value that indicates whether the template should automatically hide the navigation bar.
- [var hidesButtonsWithNavigationBar: Bool](./hidesbuttonswithnavigationbar.md)
  A Boolean value that tells the system to hide the map buttons when hiding the navigation bar.
- [var guidanceBackgroundColor: UIColor](./guidancebackgroundcolor.md)
  The background color the map template uses when displaying guidance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/mapbuttons)*