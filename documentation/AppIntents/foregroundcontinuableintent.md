# ForegroundContinuableIntent

**Framework**: App Intents  
**Kind**: protocol

A protocol you use for app intents which begin their work with the app in the background but may request to continue in the foreground.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst ?+
- macOS 13.3+
- tvOS 16.4+
- visionOS ?+
- watchOS 9.4+

## Declaration

```swift
protocol ForegroundContinuableIntent : AppIntent
```

#### Overview

This protocol is deprecated, please include `.foreground(.dynamic)` in the `supportedModes` of your app intent instead. For backward compatibility, you can provide conformance to this protocol in an extension, for example:

```swift
@available(*, deprecated)
extension OrderSoupIntent: ForegroundContinuableIntent {}
```

## Topics

### Instance Methods
- [func needsToContinueInForegroundError(IntentDialog?, continuation: (() async throws -> Void)?) -> AppIntentError](foregroundcontinuableintent/needstocontinueinforegrounderror(_:continuation:).md)
  A method you call to ask a person to continue an intent’s action in the foreground after it encounters an error.
- [func requestToContinueInForeground<ResultValue>(IntentDialog?, continuation: () async throws -> ResultValue) async throws -> ResultValue](foregroundcontinuableintent/requesttocontinueinforeground(_:continuation:).md)
  A method you call to ask a person to continue an action in the foreground.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.
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
- [protocol URLRepresentableIntent](urlrepresentableintent.md)
  An app intent with a URL representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/foregroundcontinuableintent)*