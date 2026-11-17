# instrumentClusterController

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The controller object you use to present your map content in the instrument cluster.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var instrumentClusterController: CPInstrumentClusterController { get }
```

```objc
@property (nonatomic, strong, readonly, nonnull) CPInstrumentClusterController * instrumentClusterController;
```

## Discussion

This property contains the interface controller you use to build your app’s instrument-cluster interface. CarPlay apps use a template-based approach to presenting content, which automatically adapts your interface to different vehicles and display sizes. Each template contains the data to display and the expected presentation style. The interface controller creates the views necessary to display that content in the instrument cluster.

## See Also

### Managing the scene’s interface
- [var contentStyle: UIUserInterfaceStyle](./contentstyle.md)
  The current interface style for the instrument-cluster content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscene/instrumentclustercontroller)*