# setUniform(_:named:)

**Framework**: Compute Graph  
**Kind**: method

Finds the named uniform and sets it to the given BitwiseCopyable value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
@discardableResult
final func setUniform<V>(_ value: V, named name: String) -> Bool where V : BitwiseCopyable
```

#### Discussion

Returns true if the value was found and set successfully


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/setuniform(_:named:))*