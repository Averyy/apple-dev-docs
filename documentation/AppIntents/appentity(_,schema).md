# AppEntity(_:schema:)

**Framework**: App Intents  
**Kind**: macro  
**Role**: Macro

Marks a transient entity that conforms to a schema as one whose values the model can generate on its own.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@attached(memberAttribute)
@attached(extension, conformances: GenerableEntity, AppEntity, AssistantSchemaEntity, FileEntity, UniqueAppEntity, URLRepresentableEntity, names: named(__appSchemaEntity)) macro AppEntity<T>(_ traits: AppEntityTraits, schema: T) where T : AppSchemaEntity
```

## Overview

Use this macro in place of `@AppEntity(schema:)`. It adds everything `@AppEntity(schema:)` adds, plus a [`GenerableEntity`](./generableentity.md) conformance.

## Parameters

- `traits`: The entity’s roles, such as `.generable` or `[.generable]`.
- `schema`: The schema the entity conforms to.

## See Also

### Entity support
- [protocol GenerableEntity](./generableentity.md)
  An interface that tells a model it can create an entity and fill in its properties directly.
- [macro AppEntity(AppEntityTraits)](./appentity%28_%29.md)
  Marks a transient entity whose values the model can generate on its own.
- [macro ComputedProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?)](./computedproperty%28title,description,authenticationpolicy,visibility%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?, customIndexingKey: CSCustomAttributeKey)](./computedproperty%28title,description,authenticationpolicy,visibility,customindexingkey%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro ComputedProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./computedproperty%28title,description,authenticationpolicy,visibility,indexingkey%29.md)
  A macro that adds a computed app entity property with a get accessor and an optional set accessor.
- [macro DeferredProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?)](./deferredproperty%28title,description,authenticationpolicy,visibility%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [macro DeferredProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?, indexingKey: PartialKeyPath<CSSearchableItemAttributeSet>)](./deferredproperty%28title,description,authenticationpolicy,visibility,indexingkey%29.md)
  A macro that adds an asynchronous app entity property with an asynchronous get accessor.
- [struct AppEntityTraits](./appentitytraits.md)
  The roles an app entity takes on, passed to `@AppEntity`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentity(_:schema:))*