# functionalName

**Framework**: RealityKit  
**Kind**: property

The name of the functional operation this definition implements.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var functionalName: String { get }
```

#### Discussion

Unlike [`name`](shadergraph/nodedefinition/name.md), the functional name omits type information and is shared by all definitions that implement the same operation across different types. For example, `ND_atan2_float` and `ND_atan2_vector2` both have the functional name `"atan2"`.

Use this value with [`definitions(function:inputs:)`](shadergraph/nodelibrary/definitions(function:inputs:).md) to find all type variants of an operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/nodedefinition/functionalname)*