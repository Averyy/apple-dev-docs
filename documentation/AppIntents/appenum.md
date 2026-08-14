# AppEnum

**Framework**: App Intents  
**Kind**: protocol

An interface to express that a custom type has a predefined, static set of values.

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

When you want an app intent parameter or app entity property to have a fixed set of values, set the type of the underlying property to one that adopts the `AppEnum` protocol. In custom code, you use enumerations to limit the number of values available to a property of that type. For example, a fitness app might specify the available workout types using an enumeration instead of a string, because the enumeration requires someone to choose only known values. The `AppEnum` protocol adds metadata that Siri and other system features require to interact with your enumeration or custom type.

Add the `AppEnum` protocol to an existing enumeration or type you plan to use in an app intent or app entity. For best results, base your enumeration on a type that’s easily convertible to a string such as the [`String`](https://developer.apple.com/documentation/swift/string) or [`Int`](https://developer.apple.com/documentation/swift/int) type.

The `AppEnum` protocol adds conformance to several other protocols to your type, including the [`TypeDisplayRepresentable`](typedisplayrepresentable.md) and [`CaseDisplayRepresentable`](casedisplayrepresentable.md) protocols. You’re responsible for implementing these protocols and providing descriptions of your type and each of the cases it contains. The following example shows an enumeration that a workout app uses to specify the available activities. The implementations of the [`typeDisplayRepresentation`](typedisplayrepresentable/typedisplayrepresentation.md) and [`caseDisplayRepresentations`](casedisplayrepresentable/casedisplayrepresentations.md) properties provide the protocol-mandated descriptions of the type and each activity. The system uses your descriptions in dialogs and to resolve parameters more quickly.

```swift
enum ActivityStyle: String, AppEnum {
    case biking
    case equestrian
    case hiking
    case jogging
    case crossCountrySkiing
    case snowshoeing

    // Describe the overall type.
    static var typeDisplayRepresentation: TypeDisplayRepresentation {
        TypeDisplayRepresentation(
            name: LocalizedStringResource("Activity style", table: "AppIntents"),
            numericFormat: LocalizedStringResource("\(placeholder: .int) data", table: "AppIntents"))
    }

    // Describe the individual cases.
    static var caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        .biking: DisplayRepresentation(title: "Biking", subtitle: "Mountain bike ride"),
        .equestrian: DisplayRepresentation(title: "Equestrian", subtitle: "Equestrian sports"),
        .hiking: DisplayRepresentation(title: "Hiking", subtitle: "A lengthy outdoor walk"),
        .jogging: DisplayRepresentation(title: "Jogging", subtitle: "A gentle run"),
        .crossCountrySkiing: DisplayRepresentation(title: "Skiing", subtitle: "Cross-country skiing"),
        .snowshoeing: DisplayRepresentation(title: "Snowshoeing", subtitle: "Walking in the snow")
    ]
}
```

> **Note**: Don’t adopt the [`AppEntity`](appentity.md) and `AppEnum` protocols in the same type. An app entity type represents data that can change dynamically, whereas an `AppEnum` represents static data that doesn’t change.

## Topics

### Resolving the type
- [static var defaultResolverSpecification: some ResolverSpecification](appenum/defaultresolverspecification.md)
### URL representation
- [struct EnumURLRepresentation](enumurlrepresentation.md)
  The type that provides the URL for an app enum.

## Relationships

### Inherits From
- [AppValue](appvalue.md)
- [CaseDisplayRepresentable](casedisplayrepresentable.md)
- [CaseIterable](../swift/caseiterable.md)
- [CustomLocalizedStringResourceConvertible](../foundation/customlocalizedstringresourceconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
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