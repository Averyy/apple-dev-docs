# setUniformValue(_:at:)

**Framework**: Compute Graph  
**Kind**: method

Copies the contents of `value` into the location specified by `relocation`

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
final func setUniformValue<V>(_ value: V, at location: ComputeNodeGraph.Assembly.Location) where V : BitwiseCopyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/setuniformvalue(_:at:))*