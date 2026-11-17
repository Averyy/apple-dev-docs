# backButton

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A button you use to implement custom transitions.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var backButton: CPBarButton? { get set }
```

```objc
@property (nonatomic, strong, nullable) CPBarButton * backButton;
```

## Discussion

All CarPlay templates except the root template have a back button with a standard appearance. When the value of this property is `nil`, the button responds to interactions by dismissing the current template and displaying the previous template on the navigation stack. In CarPlay template implementations, the default value of this property is `nil`.

To provide an app-specific action for the back button, assign a custom button to this property. CarPlay doesn’t use your custom button’s appearance, but it does run your handler when interactions with the back button occur.

## See Also

### Providing navigation bar buttons
- [var leadingNavigationBarButtons: [CPBarButton]](./leadingnavigationbarbuttons.md)
  Additional buttons to display at the leading edge of the navigation bar.
- [var trailingNavigationBarButtons: [CPBarButton]](./trailingnavigationbarbuttons.md)
  Additional buttons to display at the trailing edge of the navigation bar.
- [class CPBarButton](../cpbarbutton.md)
  A button that appears in a navigation bar.
- [class CPMessageComposeBarButton](../cpmessagecomposebarbutton.md)
  A button that activates Siri and initiates the process for composing a message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpbarbuttonproviding/backbutton)*