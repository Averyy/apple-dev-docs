# trailingNavigationBarButtons

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Additional buttons to display at the trailing edge of the navigation bar.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var trailingNavigationBarButtons: [CPBarButton] { get set }
```

```objc
@property (nonatomic, strong) NSArray<CPBarButton *> * trailingNavigationBarButtons;
```

## Discussion

Add no more than two buttons to this property. If you specify more than two buttons, CarPlay displays the first two in the array and ignores the rest. In CarPlay template implementations, the default value of this property is an empty array.

## See Also

### Providing navigation bar buttons
- [var backButton: CPBarButton?](./backbutton.md)
  A button you use to implement custom transitions.
- [var leadingNavigationBarButtons: [CPBarButton]](./leadingnavigationbarbuttons.md)
  Additional buttons to display at the leading edge of the navigation bar.
- [class CPBarButton](../cpbarbutton.md)
  A button that appears in a navigation bar.
- [class CPMessageComposeBarButton](../cpmessagecomposebarbutton.md)
  A button that activates Siri and initiates the process for composing a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbuttonproviding/trailingnavigationbarbuttons)*