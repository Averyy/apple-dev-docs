# CustomIntentMigratedAppIntent

**Framework**: App Intents  
**Kind**: protocol

An interface for replacing a custom SiriKit intent that allows existing shortcuts and donations to continue working.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
protocol CustomIntentMigratedAppIntent : AppIntent
```

## Topics

### Specifying the migrated intent’s class name
- [static var intentClassName: String](customintentmigratedappintent/intentclassname.md)
  The name of the SiriKit Intent class that this app intent replaces.

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/customintentmigratedappintent)*