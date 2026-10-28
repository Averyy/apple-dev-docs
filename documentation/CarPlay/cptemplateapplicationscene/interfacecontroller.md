# interfaceController

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The controller that manages the scene’s user interface.

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

Use this property to access the interface controller CarPlay creates when the scene connects, which you then use to manage your templates.

## See Also

### Accessing the Interface Controller
- [class CPInterfaceController](../cpinterfacecontroller.md)
  A controller that manages the templates for constructing a scene’s user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene/interfacecontroller)*