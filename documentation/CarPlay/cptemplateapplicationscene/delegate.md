# delegate

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The custom object you provide to handle scene’s life-cycle events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var delegate: (any CPTemplateApplicationSceneDelegate)? { get set }
```

```objc
@property (nonatomic, strong, nullable) id<CPTemplateApplicationSceneDelegate> delegate;
```

## Discussion

The scene’s delegate object serves as the entry point to your CarPlay app and handles high-level interactions involving the scene. The delegate is a custom type you define in your app and associate with your scene in the scene manifest of your app’s information property list file. When launching your CarPlay app, the system instantiates your delegate type and places the resulting object in this property.

## See Also

### Responding to scene life-cycle events
- [protocol CPTemplateApplicationSceneDelegate](../cptemplateapplicationscenedelegate.md)
  Methods for responding to  life-cycle events in your app’s scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene/delegate)*