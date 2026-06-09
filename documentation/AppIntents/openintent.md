# OpenIntent

**Framework**: App Intents  
**Kind**: protocol

Open the associated item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
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

Use this intent to open both dynamic items such as [`AppEntity`](appentity.md) and static items such as an [`AppEnum`](appenum.md) with voice commands; for example, “Open ‘Vacation Ideas’” or “Open bookmarks”.

## Topics

### Associated Types
- [associatedtype Value : AppValue](openintent/value.md)
### Instance Properties
- [var target: Self.Value](openintent/target.md)

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [struct OpenURLIntent](openurlintent.md)
  An intent that opens a universal link.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/openintent)*