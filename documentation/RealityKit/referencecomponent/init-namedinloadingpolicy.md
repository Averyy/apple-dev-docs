# init(named:in:loadingPolicy:)

**Framework**: RealityKit  
**Kind**: init

Creates a reference component with a name, loading policy, and bundle.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(named name: String, in bundle: Bundle, loadingPolicy: ReferenceComponent.LoadingPolicy = .onDemand)
```

## Parameters

- `name`: The name of the entity to load.
- `bundle`: The bundle to search for the resource.
- `loadingPolicy`: A loading policy indicating when the app loads the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/referencecomponent/init(named:in:loadingpolicy:))*