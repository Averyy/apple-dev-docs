# AppEnum

**Framework**: App Intents  
**Kind**: protocol

An interface to express that a custom type has a predefined, static set of valid values to display.

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
protocol AppEnum : AppValue, StaticDisplayRepresentable, RawRepresentable where Self.RawValue : LosslessStringConvertible
```

## Mentions

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
- [Defining app entities for your custom data types](defining-app-entities-for-your-custom-data-types.md)
- [Responding to the Action button on Apple Watch Ultra](actionbuttonarticle.md)
- [Getting started with the App Intents framework](getting-started-with-the-app-intents-framework.md)

#### Overview

Adopt the [`AppEnum`](appenum.md) protocol in a type that has a known set of valid values. You might use this protocol to specify that a variable of one of your intents has a fixed set of possible values. For example, you might use a variable to specify whether to navigate to the next or previous track in a music playlist.

Because this type conforms to the [`StaticDisplayRepresentable`](staticdisplayrepresentable.md) protocol, provide a string-based representation of your type’s values in your implementation. For example, provide descriptions for each case of an `enum` type in the inherited [`caseDisplayRepresentations`](casedisplayrepresentable/casedisplayrepresentations.md) property.

## Topics

### Resolving the type
- [static var defaultResolverSpecification: some ResolverSpecification](appenum/defaultresolverspecification.md)
### URL representation
- [struct EnumURLRepresentation](enumurlrepresentation.md)
  The URL representation of an app enum.

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
- [AppUnionValueCasesProviding](appunionvaluecasesproviding.md)
- [AssistantEnum](assistantenum.md)
- [AssistantSchemaEnum](assistantschemaenum.md)
- [URLRepresentableEnum](urlrepresentableenum.md)
### Conforming Types
- [StringSearchScope](stringsearchscope.md)
- [VideoCategory](videocategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appenum)*