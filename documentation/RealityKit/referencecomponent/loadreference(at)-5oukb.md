# loadReference(at:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Synchronously loads another entity file that an entity depends on.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
static func loadReference(at entity: Entity) throws
```

**Other overloads**:

```swift
@MainActor
static func loadReference(at entity: Entity) async throws
```

## Parameters

- `entity`: The entity that holds the [`ReferenceComponent`](../referencecomponent.md) to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/referencecomponent/loadreference(at:)-5oukb)*