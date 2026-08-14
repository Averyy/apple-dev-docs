# SetValueIntent

**Framework**: App Intents  
**Kind**: protocol

An intent that contains a value which can be set.

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol OpenIntent](openintent.md)
  An app intent that opens and displays a specific item in your app’s interface.
- [struct OpenURLIntent](openurlintent.md)
  An app intent that opens one of your universal links and displays its contents.
- [protocol DeleteIntent](deleteintent.md)
  Delete the associated entity(s).
- [protocol DeprecatedAppIntent](deprecatedappintent.md)
  An app intent that marks an action as deprecated and informs people which action to use instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/setvalueintent)*