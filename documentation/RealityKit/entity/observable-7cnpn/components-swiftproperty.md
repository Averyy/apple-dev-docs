# components

**Framework**: RealityKit  
**Kind**: property

A “pass through” to the underlying ComponentSet but with the added effect of marking those component keypaths as “accessed” when a property is read. Mutations to any accessed components will cause any observers to be triggered.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
var components: Entity.Observable.Components { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/observable-7cnpn/components-swift.property)*