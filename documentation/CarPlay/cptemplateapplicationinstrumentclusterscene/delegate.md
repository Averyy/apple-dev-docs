# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The custom object you provide to handle scene’s life-cycle events.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
var delegate: (any CPTemplateApplicationInstrumentClusterSceneDelegate)? { get set }
```

```objc
@property (nonatomic, strong, nullable) id<CPTemplateApplicationInstrumentClusterSceneDelegate> delegate;
```

## Discussion

The scene’s delegate object serves as the entry point to your CarPlay app and handles high-level interactions involving the scene. The delegate is a custom type you define in your app and associate with your scene in the scene manifest of your app’s information property list file. When launching your CarPlay app, the system instantiates your delegate type and places the resulting object in this property.

## See Also

### Responding to scene life-cycle events
- [protocol CPTemplateApplicationInstrumentClusterSceneDelegate](../cptemplateapplicationinstrumentclusterscenedelegate.md)
  The methods for responding to the life cycle events in your app’s instrument cluster scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscene/delegate)*