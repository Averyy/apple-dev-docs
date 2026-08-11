# DeleteIntent

**Framework**: App Intents  
**Kind**: protocol

Delete the associated entity(s).

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
  An app intent that opens and displays a specific item in your app’s interface.
- [struct OpenURLIntent](openurlintent.md)
  An app intent that opens one of your universal links and displays its contents.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/deleteintent)*