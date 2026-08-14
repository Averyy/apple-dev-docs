# OpenIntent

**Framework**: App Intents  
**Kind**: protocol

An app intent that opens and displays a specific item in your app’s interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
protocol OpenIntent : SystemIntent
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)
- [Getting started with the App Intents framework](getting-started-with-the-app-intents-framework.md)
- [Making app entities available in Spotlight](making-app-entities-available-in-spotlight.md)

#### Overview

Use this protocol to create an app intent that opens the app and displays a specific item. The [`target`](openintent/target.md) property contains the item to display and is typically an [`AppEntity`](appentity.md) or [`AppEnum`](appenum.md) type you define. For example, Spotlight can populate this property with an entity someone found during a search of your app’s content.

> **Note**: If your app intent type implements the [`URLRepresentableIntent`](urlrepresentableintent.md) protocol, or if the [`target`](openintent/target.md) parameter contains a type with a URL representation, provide an implementation of your [`perform()`](appintent/perform().md) method that returns a result and does nothing else. When a URL is present, the system opens the item using your app’s URL support instead.

The system automatically brings your app to the foreground to run this app intent. If your app intent adopts the [`TargetContentProvidingIntent`](targetcontentprovidingintent.md) or [`UISceneAppIntent`](uisceneappintent.md) protocol, the system also directs the app intent to one of your app’s scenes first so you can configure the scene’s views. If your app intent type doesn’t support these protocols, use your [`perform()`](appintent/perform().md) method implementation to update your app’s interface and display the item.

## Topics

### Associated Types
- [associatedtype Value : AppValue](openintent/value.md)
  The type of the item to open.
### Instance Properties
- [var target: Self.Value](openintent/target.md)
  The item to open in your app.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [struct OpenURLIntent](openurlintent.md)
  An app intent that opens one of your universal links and displays its contents.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openintent)*