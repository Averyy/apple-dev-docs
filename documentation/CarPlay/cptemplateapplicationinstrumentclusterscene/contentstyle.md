# contentStyle

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The current interface style for the instrument-cluster content.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var contentStyle: UIUserInterfaceStyle { get }
```

```objc
@property (nonatomic, readonly) UIUserInterfaceStyle contentStyle;
```

## Discussion

This property indicates whether your app displays instrument-cluster content using a light, dark, or unspecified appearance. The vehicle settings define the style, which can change while CarPlay is active. When the style changes, CarPlay reports the change to the [`contentStyleDidChange(_:)`](../cptemplateapplicationinstrumentclusterscenedelegate/contentstyledidchange%28_%29.md) method of the scene’s delegate object.

## See Also

### Managing the scene’s interface
- [var instrumentClusterController: CPInstrumentClusterController](./instrumentclustercontroller.md)
  The controller object you use to present your map content in the instrument cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscene/contentstyle)*