# init(definition:nodeResourceMapping:skeletonResource:)

**Framework**: RealityKit  
**Kind**: init

Compile a new resource from data, throws on failure.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(definition: Data, nodeResourceMapping: [Int : AnimationResource] = [:], skeletonResource: SkeletonResource) throws
```

## See Also

- [static func validate(definition: Data, nodeResourceMapping: [Int : AnimationResource], skeletonResource: SkeletonResource) -> [String]](animationgraphresource/validate(definition:noderesourcemapping:skeletonresource:).md)
  Run the compiler and return all graph errors without producing a resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationgraphresource/init(definition:noderesourcemapping:skeletonresource:))*