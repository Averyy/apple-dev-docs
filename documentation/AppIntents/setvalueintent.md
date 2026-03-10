# SetValueIntent

**Framework**: App Intents  
**Kind**: protocol

An intent that contains a value which can be set.

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
protocol SetValueIntent<ValueType> : AppIntent
```

#### Overview

```swift
struct ToggleSilentMode: SetValueIntent {
   static var title = LocalizedStringResource("Silent Mode")

   @Parameter(title: "Silent")
   var value: Bool
}
```

## Topics

### Associated Types
- [associatedtype ValueType : _IntentValue](setvalueintent/valuetype.md)
### Instance Properties
- [var value: Self.ValueType](setvalueintent/value.md)

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
- [protocol ForegroundContinuableIntent](foregroundcontinuableintent.md)
  A protocol you use for app intents which begin their work with the app in the background but may request to continue in the foreground.
- [protocol OpenIntent](openintent.md)
  Open the associated item.
- [struct OpenURLIntent](openurlintent.md)
  An intent that opens a universal link.
- [protocol ProgressReportingIntent](progressreportingintent.md)
  An intent that reports progress to the system during its execution
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/setvalueintent)*