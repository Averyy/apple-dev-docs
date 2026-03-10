# URLRepresentableIntent

**Framework**: App Intents  
**Kind**: protocol

An app intent with a URL representation.

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
protocol URLRepresentableIntent : AppIntent
```

#### Overview

Add support for `URLRepresentableIntent` to your app intents to add a URL representation. This allows Siri and Shortcuts to treat the intent like a universal link to specific content, allowing actions to open the URL or to make it sharable.

Note that you need to use a universal link for your URL representation, you can’t use a custom URL scheme. For more information about universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

## Topics

### Type Aliases
- [URLRepresentableIntent.URLRepresentation](urlrepresentableintent/urlrepresentation-swift.typealias.md)
### Type Properties
- [static var urlRepresentation: Self.URLRepresentation](urlrepresentableintent/urlrepresentation-4fzwq.md)

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [OpenURLIntent](openurlintent.md)

## See Also

- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.
- [protocol ForegroundContinuableIntent](foregroundcontinuableintent.md)
  A protocol you use for app intents which begin their work with the app in the background but may request to continue in the foreground.
- [protocol OpenIntent](openintent.md)
  Open the associated item.
- [struct OpenURLIntent](openurlintent.md)
  An intent that opens a universal link.
- [protocol ProgressReportingIntent](progressreportingintent.md)
  An intent that reports progress to the system during its execution
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.
- [protocol SnippetIntent](snippetintent.md)
  An app intent that presents an interactive snippet onscreen.
- [protocol SystemIntent](systemintent.md)
  Designates intent types provided by App Intents.
- [protocol TargetContentProvidingIntent](targetcontentprovidingintent.md)
- [protocol UISceneAppIntent](uisceneappintent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/urlrepresentableintent)*