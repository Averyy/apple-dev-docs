# UISceneAppIntent

**Framework**: App Intents  
**Kind**: protocol

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol UISceneAppIntent : TargetContentProvidingIntent
```

## Topics

### Instance Properties
- [var uiScene: UIScene?](uisceneappintent/uiscene.md)
### Instance Methods
- [func performNavigation(forScene: UIScene)](uisceneappintent/performnavigation(forscene:).md)

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [TargetContentProvidingIntent](targetcontentprovidingintent.md)

## See Also

- [protocol AppIntentSceneDelegate](appintentscenedelegate.md)
  Implement this protocol on your UIScene delegate to handle AppIntent invocations targeting a specific scene
- [protocol TargetContentProvidingIntent](targetcontentprovidingintent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uisceneappintent)*