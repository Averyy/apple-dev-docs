# AppEnum

**Framework**: App Intents  
**Kind**: protocol

An interface to express that a custom type has a predefined, static set of valid values to display.

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
protocol AppEnum : AppValue, StaticDisplayRepresentable, RawRepresentable where Self.RawValue : LosslessStringConvertible
```

## Mentions

- [Integrating actions with Siri and Apple Intelligence](integrating-actions-with-siri-and-apple-intelligence.md)
- [Integrating custom data types into your intents](integrating-custom-types-into-your-intents.md)
- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)

#### Overview

Adopt the [`AppEnum`](appenum.md) protocol in a type that has a known set of valid values. You might use this protocol to specify that a variable of one of your intents has a fixed set of possible values. For example, you might use a variable to specify whether to navigate to the next or previous track in a music playlist.

Because this type conforms to the [`StaticDisplayRepresentable`](staticdisplayrepresentable.md) protocol, provide a string-based representation of your type’s values in your implementation. For example, provide descriptions for each case of an `enum` type in the inherited [`caseDisplayRepresentations`](casedisplayrepresentable/casedisplayrepresentations.md) property.

## Topics

### Resolving the type
- [static var defaultResolverSpecification: some ResolverSpecification](appenum/defaultresolverspecification.md)

## Relationships

### Inherits From
- [AppValue](appvalue.md)
- [CaseDisplayRepresentable](casedisplayrepresentable.md)
- [CaseIterable](../Swift/CaseIterable.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [StaticDisplayRepresentable](staticdisplayrepresentable.md)
- [TypeDisplayRepresentable](typedisplayrepresentable.md)
### Inherited By
- [AssistantEnum](assistantenum.md)
- [AssistantSchemaEnum](assistantschemaenum.md)
- [URLRepresentableEnum](urlrepresentableenum.md)
### Conforming Types
- [StringSearchScope](stringsearchscope.md)
- [VideoCategory](videocategory.md)

## See Also

- [class EntityProperty](entityproperty.md)
  A property wrapper that exposes the associated property to the system.
- [protocol AppValue](appvalue.md)
  An interface that describes conceptual types you use in app intents.
- [protocol AnyIntentValue](anyintentvalue.md)
  A type the system uses to access a parameter or property value.
- [protocol URLRepresentableEnum](urlrepresentableenum.md)
  An app enum with a URL representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appenum)*