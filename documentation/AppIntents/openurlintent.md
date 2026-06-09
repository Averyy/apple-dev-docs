# OpenURLIntent

**Framework**: App Intents  
**Kind**: struct

An intent that opens a universal link.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct OpenURLIntent
```

#### Overview

Return an `OpenURLIntent` as the [`IntentResult`](intentresult.md) of another app intent’s [`perform()`](appintent/perform().md) method or use place the intent on a button that appears on an interactive widget or Live Activity.

Note that you need to use a universal link for your URL representation, you can’t use a custom URL scheme. For more information about universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

## Topics

### Initializers
- [init(URL)](openurlintent/init(_:).md)
- [init(urlRepresentable: some URLRepresentableEnum) throws](openurlintent/init(urlrepresentable:)-53fa0.md)
- [init(urlRepresentable: some URLRepresentableEntity) async throws](openurlintent/init(urlrepresentable:)-8r4bl.md)
### Instance Properties
- [var $url: IntentParameter<URL>](openurlintent/$url.md)
- [var url: URL](openurlintent/url.md)

## Relationships

### Conforms To
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)
- [URLRepresentableIntent](urlrepresentableintent.md)

## See Also

- [protocol OpenIntent](openintent.md)
  Open the associated item.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openurlintent)*