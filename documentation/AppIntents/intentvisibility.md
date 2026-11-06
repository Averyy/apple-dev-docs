# IntentVisibility

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

A value that configures how a property is available to system features, such as Siri and Shortcuts, if at all.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
struct IntentVisibility
```

## Overview

System features such as Siri and Shortcuts list an app entity’s properties to people and to the model when you apply the [`default`](./intentvisibility/default.md) option. However, you can limit a property’s visibility to just your app and its extensions by applying the [`internal`](./intentvisibility/internal.md) option. For example, apps typically apply this option to properties with sensitive information.

```swift
struct Contact: AppEntity {
    @Property(title: "Tax ID", visibility: .internal)
    var taxID: String
}
```

> **Note**: Don’t combine the [`internal`](./intentvisibility/internal.md) option with an indexing key for Spotlight, such as `indexingKey` or `customIndexingKey`, because the keys make the property discoverable from Spotlight.

## Topics

### Type Properties
- [static var `default`: IntentVisibility](./intentvisibility/default.md)
  A visibility option that makes the property available to your app and to system features, such as Siri and Shortcuts.
- [static var `internal`: IntentVisibility](./intentvisibility/internal.md)
  A visibility option that limits the property to your app and its extensions.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Tool support
- [macro AppIntent(AppIntentTraits)](./appintent%28_%29.md)
  Makes an existing app intent available to Siri as a tool.
- [macro AppIntent<T>(AppIntentTraits, schema: T)](./appintent%28_,schema%29.md)
  Makes an app intent that conforms to a schema available to Siri as a tool.
- [struct AppIntentTraits](./appintenttraits.md)
  The roles an app intent takes on, passed to `@AppIntent`.
- [protocol ToolIntent](./toolintent.md)
  A protocol that identifies an app intent that Siri can call while handling a person’s request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvisibility)*