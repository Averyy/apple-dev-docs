# ComputedProperty(title:description:authenticationPolicy:visibility:customIndexingKey:)

**Framework**: App Intents  
**Kind**: macro  
**Role**: Macro

A macro that adds a computed app entity property with a get accessor and an optional set accessor.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@attached(peer, names: prefixed(`$`), prefixed(`_`))
@attached(accessor, names: named(get), named(set)) macro ComputedProperty(title: LocalizedStringResource? = nil, description: LocalizedStringResource? = nil, authenticationPolicy: IntentAuthenticationPolicy? = nil, visibility: IntentVisibility? = nil, customIndexingKey: CSCustomAttributeKey)
```

## Parameters

- `title`: A localized string resource describing the property for display in the user interface.
- `description`: Additional details about this property.
- `authenticationPolicy`: The authentication policy to enforce when the system accesses this property, or `nil` to use the entity’s policy.
- `visibility`: Whether the property is available to system features, or only to your app, or `nil` for `.default`.
- `customIndexingKey`: A custom Spotlight attribute set key for this property.

## See Also

### Entity support
- [protocol GenerableEntity](./generableentity.md)
  An interface that tells a model it can create an entity and fill in its properties directly.
- [macro AppEntity(AppEntityTraits)](./appentity%28_%29.md)
  Marks a transient entity whose values the model can generate on its own.
- [macro AppEntity<T>(AppEntityTraits, schema: T)](./appentity%28_,schema%29.md)
  Marks a transient entity that conforms to a schema as one whose values the model can generate on its own.
- [macro ComputedProperty(title: LocalizedStringResource?, description: LocalizedStringResource?, authenticationPolicy: IntentAuthenticationPolicy?, visibility: IntentVisibility?)](./computedproperty%28title,description,authenticationpolicy,visibility%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/computedproperty(title:description:authenticationpolicy:visibility:customindexingkey:))*