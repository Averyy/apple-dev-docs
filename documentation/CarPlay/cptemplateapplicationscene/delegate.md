# delegate

**Framework**: CarPlay  
**Kind**: property

The object that receives the scene’s life-cycle events.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var delegate: (any CPTemplateApplicationSceneDelegate)? { get set }
```

#### Discussion

Use this property to access the delegate object CarPlay creates from the class name you provide in the scene manifest of your app’s `Info.plist` file.

## See Also

- [protocol CPTemplateApplicationSceneDelegate](cptemplateapplicationscenedelegate.md)
  The methods for responding to the life cycle events of your app’s scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene/delegate)*