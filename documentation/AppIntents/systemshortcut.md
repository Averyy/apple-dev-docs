# SystemShortcut

**Framework**: App Intents  
**Kind**: struct

An opaque reference to a user-configured action for use in a widget button.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct SystemShortcut
```

## Mentions

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)

#### Overview

The system creates `SystemShortcut` instances to represent a person’s choice when they configure the action for a button in a widget. It can represent a custom shortcut, App Shortcut, system action, or an installed app. `SystemShortcut` only exposes metadata that the system needs to fill the configuration UI, for example, the action’s display representation. It doesn’t provide the app or widget with a custom shortcut’s actions, parameters, or implementation details.

## Topics

### Resolving the type
- [static let defaultResolverSpecification: EmptyResolverSpecification<SystemShortcut>](systemshortcut/defaultresolverspecification.md)
- [SystemShortcut.Specification](systemshortcut/specification.md)
- [SystemShortcut.ValueType](systemshortcut/valuetype.md)
- [SystemShortcut.UnwrappedType](systemshortcut/unwrappedtype.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [DisplayRepresentable](displayrepresentable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [InstanceDisplayRepresentable](instancedisplayrepresentable.md)
- [IntentValueConvertible](intentvalueconvertible.md)
- [IntentValueExpressing](intentvalueexpressing.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)

## See Also

- [init(shortcut: SystemShortcut)](runsystemshortcutintent/init(shortcut:).md)
  Creates an intent that performs a person’s configured action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/systemshortcut)*