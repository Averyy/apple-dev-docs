# buildExpression(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Treats a `[Joint]` value in the closure body as a list of children of the parent. All elements become children, in array order; they are siblings of any other joints declared in the same closure body.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static func buildExpression(_ expression: [SkeletonResource.Joint]) -> [SkeletonResource.Joint]
```

**Other overloads**:

```swift
static func buildExpression(_ expression: SkeletonResource.Joint) -> [SkeletonResource.Joint]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/skeletonresource/jointbuilder/buildexpression(_:)-10xi7)*