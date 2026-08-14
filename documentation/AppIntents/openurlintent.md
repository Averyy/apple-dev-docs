# OpenURLIntent

**Framework**: App Intents  
**Kind**: struct

An app intent that opens one of your universal links and displays its contents.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct OpenURLIntent
```

#### Overview

This app intent uses your app’s existing universal link support to open the specified URL. Universal links are a stable and consistent way to refer to the same content in your app or website. Apps that support universal links can return this type as the result of another app intent’s [`perform()`](appintent/perform().md) method to display specific content. You can also place the app intent on a button in an interactive widget or Live Activity. When the app intent runs, the system sends the URL to your app’s URL handling code so you can open the referenced content.

The system automatically brings your app to the foreground to run an app intent of this type. If your app intent adopts the [`TargetContentProvidingIntent`](targetcontentprovidingintent.md) or [`UISceneAppIntent`](uisceneappintent.md) protocol, the system directs the app intent to one of your app’s scenes first so you can configure the scene’s views. If your app intent type doesn’t support these protocols, use the [`perform()`](appintent/perform().md) method to update your app’s interface.

For information about how to adopt universal links in your app, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).

## Topics

### Initializers
- [init(URL)](openurlintent/init(_:).md)
  Configures the app intent with the provided URL.
- [init(urlRepresentable: some URLRepresentableEnum) throws](openurlintent/init(urlrepresentable:)-53fa0.md)
  Configures the app intent using an app enum with a URL representation.
- [init(urlRepresentable: some URLRepresentableEntity) async throws](openurlintent/init(urlrepresentable:)-8r4bl.md)
  Configures the app intent using an app entity with a URL representation.
### Instance Properties
- [var $url: IntentParameter<URL>](openurlintent/$url.md)
- [var url: URL](openurlintent/url.md)
  The universal link you use to locate your app’s content.

## Relationships

### Conforms To
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SystemIntent](systemintent.md)
- [URLRepresentableIntent](urlrepresentableintent.md)

## See Also

- [protocol OpenIntent](openintent.md)
  An app intent that opens and displays a specific item in your app’s interface.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent)*