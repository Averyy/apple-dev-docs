# interfaceController

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The controller object you use to present your app’s interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var interfaceController: CPInterfaceController { get }
```

```objc
@property (nonatomic, strong, readonly, nonnull) CPInterfaceController * interfaceController;
```

## Discussion

This property contains the interface controller you use to build the interface for your CarPlay app. CarPlay apps use a template-based approach to presenting content, which insulates you from having to customize your interface for different vehicles and different display sizes. Each template contains the data to display and the expected presentation style. The interface controller creates the views necessary to display that content on the current vehicle’s display.

All apps use the interface controller in this property to build their interface. If you’re building a navigation app, you present most of your content using this interface controller but also add your custom map content to the scene’s window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene/interfacecontroller)*