# automaticallyHidesNavigationBar

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the template should automatically hide the navigation bar.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var automaticallyHidesNavigationBar: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL automaticallyHidesNavigationBar;
```

## Discussion

The default is [`true`](../../Swift/true.md).

## See Also

### Configuring the map template
- [var hidesButtonsWithNavigationBar: Bool](./hidesbuttonswithnavigationbar.md)
  A Boolean value that tells the system to hide the map buttons when hiding the navigation bar.
- [var guidanceBackgroundColor: UIColor](./guidancebackgroundcolor.md)
  The background color the map template uses when displaying guidance.
- [var mapButtons: [CPMapButton]](./mapbuttons.md)
  An array of map buttons on the trailing bottom corner of the map template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplate/automaticallyhidesnavigationbar)*