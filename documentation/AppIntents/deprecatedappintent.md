# DeprecatedAppIntent

**Framework**: App Intents  
**Kind**: protocol

An app intent that marks an action as deprecated and informs people which action to use instead.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
protocol DeprecatedAppIntent : AppIntent
```

## Topics

### Associated Types
- [associatedtype ReplacementIntent : AppIntent = Never](deprecatedappintent/replacementintent.md)
### Type Properties
- [static var deprecation: IntentDeprecation<Self.ReplacementIntent>](deprecatedappintent/deprecation.md)

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol OpenIntent](openintent.md)
  Open the associated item.
- [struct OpenURLIntent](openurlintent.md)
  An intent that opens a universal link.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/deprecatedappintent)*