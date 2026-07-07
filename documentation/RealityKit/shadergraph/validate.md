# validate()

**Framework**: RealityKit  
**Kind**: method

Checks whether the graph is well-formed without producing a Metal library.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func validate() -> Bool
```

#### Return Value

`true` if the graph passes front-end validation, `false` otherwise.

#### Discussion

Runs the ShaderGraph compiler front end — parsing, graph construction, and the transform pipeline — but stops short of stitching the graph into a Metal library. Use this to catch structural problems before paying the cost of a full compile.

Validation is cheaper than [`ShaderGraphMaterial`](shadergraphmaterial.md) compilation, but the exact amount of work skipped is not guaranteed and may change over time. A graph that passes [`validate()`](shadergraph/validate().md) may still fail later during Metal library generation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/validate())*