# init(identifier:title:description:authenticationPolicy:visibility:asyncGetter:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Creates an app intent entity property.  Do not call this directly, use @ComputedProperty or @DeferredProperty

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
convenience init<Entity>(identifier: String, title: LocalizedStringResource? = nil, description: LocalizedStringResource? = nil, authenticationPolicy: IntentAuthenticationPolicy? = nil, visibility: IntentVisibility? = nil, asyncGetter: @escaping @Sendable (Entity) async throws -> Value) where Entity : AppEntity
```

Available when `Value` conforms to `_IntentValue` and `Sendable`.

## Parameters

- `identifier`: The identifier of the property
- `title`: A word or short phrase summarizing this property.
- `description`: A string that explains to the system what the property represents and what role it plays.
- `authenticationPolicy`: An authentication policy that the system enforces when accessing the property, or `nil` to apply the entity’s default policy.
- `visibility`: An option that configures how the property is available to system features, if at all, or `nil` to apply the [`default`](../intentvisibility/default.md) visibility.
- `asyncGetter`: The async getter for the property


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityproperty/init(identifier:title:description:authenticationpolicy:visibility:asyncgetter:))*