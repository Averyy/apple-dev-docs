# DeleteIntent

**Framework**: App Intents  
**Kind**: protocol

Delete the associated entity(s).

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
protocol DeleteIntent : SystemIntent
```

## Topics

### Associated Types
- [associatedtype Entity : AppEntity](deleteintent/entity.md)
### Instance Properties
- [var entities: [Self.Entity]](deleteintent/entities.md)

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SystemIntent](systemintent.md)

## See Also

- [protocol OpenIntent](openintent.md)
  Open the associated item.
- [struct OpenURLIntent](openurlintent.md)
  An intent that opens a universal link.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.
- [protocol ShowInAppSearchResultsIntent](showinappsearchresultsintent.md)
  An app intent that takes a person to search results for a specified search term.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/deleteintent)*