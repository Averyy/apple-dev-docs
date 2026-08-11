# URLRepresentableIntent

**Framework**: App Intents  
**Kind**: protocol

An interface you add to an app intent type so the system can handle it like a universal link.

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
protocol URLRepresentableIntent : AppIntent
```

#### Overview

If your app already supports universal links for content, use this protocol to express your app intent types as URLs. When your app intent supports this protocol, the system can use the provided URL to process it. For example, if your app intent supports this protocol and the [`OpenIntent`](openintent.md) protocol, the system opens the contained item by sending the URL to your app’s URL handling code, allowing you to omit the [`perform()`](appintent/perform().md) method in your type. Having a URL representation for your app intent also makes it easier to share its contents with Siri, Shortcuts, and other system features.

> ❗ **Important**: This protocol requires your app to support universal links. You can’t use this protocol with a custom URL scheme or other approaches. For information about how to add support for universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

Construct URLs using static text and the content of your app intent’s properties. For information on how to create the URL representation, see [`IntentURLRepresentation`](intenturlrepresentation.md).

## Topics

### Type Aliases
- [URLRepresentableIntent.URLRepresentation](urlrepresentableintent/urlrepresentation-swift.typealias.md)
  The type that provides the URL for the app intent.
### Type Properties
- [static var urlRepresentation: Self.URLRepresentation](urlrepresentableintent/urlrepresentation-4fzwq.md)
  The URL representation of the app intent.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [OpenURLIntent](openurlintent.md)

## See Also

- [struct IntentURLRepresentation](intenturlrepresentation.md)
  The type that provides the URL for an app intent.
- [protocol CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)
  An interface that allows a type to express its contents in a URL representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/urlrepresentableintent)*