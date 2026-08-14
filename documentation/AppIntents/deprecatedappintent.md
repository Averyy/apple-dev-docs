# DeprecatedAppIntent

**Framework**: App Intents  
**Kind**: protocol

An app intent that marks an action as deprecated and informs people which action to use instead.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol OpenIntent](openintent.md)
  An app intent that opens and displays a specific item in your app’s interface.
- [struct OpenURLIntent](openurlintent.md)
  An app intent that opens one of your universal links and displays its contents.
- [protocol SetValueIntent](setvalueintent.md)
  An intent that contains a value which can be set.
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/deprecatedappintent)*