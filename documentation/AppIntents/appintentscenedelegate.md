# AppIntentSceneDelegate

**Framework**: App Intents  
**Kind**: protocol

Implement this protocol on your UIScene delegate to handle AppIntent invocations targeting a specific scene Example:

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol AppIntentSceneDelegate : UISceneDelegate
```

#### Overview

```swift
func windowScene(_ scene: UIScene, willPerformAppIntent appIntent: any AppIntent) {
    switch appIntent {
      case let myIntent as MyIntent:
         windowScene.activationConditions.prefersToActivateForTargetContentIdentifierPredicate = NSPredicate("self == %@", myIntent.targetContentIdentifier)
    }
}
```

## Topics

### Instance Methods
- [func scene(UIScene, willPerformAppIntent: any UISceneAppIntent)](appintentscenedelegate/scene(_:willperformappintent:).md)
  Calling perform on the AppIntent provided in this delegate is a programmer error See: `UIScene.ConnectionOptions.appIntent`

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UISceneDelegate](../UIKit/UISceneDelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintentscenedelegate)*