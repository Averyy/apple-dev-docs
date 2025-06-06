# leadingNavigationBarButtons

**Framework**: CarPlay  
**Kind**: property  
**Required**: Yes

An array of bar buttons to display on the leading side of the navigation bar.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var leadingNavigationBarButtons: [CPBarButton] { get set }
```

#### Discussion

The navigation bar displays up to two buttons in the leading space. When including more than two buttons in the array, the system displays only the first two buttons.

## See Also

- [var backButton: CPBarButton?](cpbarbuttonproviding/backbutton.md)
  A button to display as the Back button on the navigation bar.
- [var trailingNavigationBarButtons: [CPBarButton]](cpbarbuttonproviding/trailingnavigationbarbuttons.md)
  An array of bar buttons to display on the trailing side of the navigation bar.
- [class CPBarButton](cpbarbutton.md)
  A button for placement in a navigation bar.
- [class CPMessageComposeBarButton](cpmessagecomposebarbutton.md)
  A button that activates Siri and initiates the compose message flow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbuttonproviding/leadingnavigationbarbuttons)*