# init(named:loadingPolicy:)

**Framework**: RealityKit  
**Kind**: init

Creates a reference component with a name and loading policy.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(named name: String, loadingPolicy: ReferenceComponent.LoadingPolicy = .onDemand)
```

#### Discussion

Place references in the app’s main bundle.

## Parameters

- `name`: The name of the entity to load.
- `loadingPolicy`: A loading policy indicating when the app loads the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/referencecomponent/init(named:loadingpolicy:))*