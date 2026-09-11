# setUniform(_:named:)

**Framework**: Compute Graph  
**Kind**: method

Finds the named uniform and sets it to the given BitwiseCopyable value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
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