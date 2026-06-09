# setUniformValue(_:at:)

**Framework**: ComputeGraph  
**Kind**: method

Copies the contents of `value` into the location specified by `relocation`

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
final func setUniformValue<V>(_ value: V, at location: ComputeNodeGraph.Assembly.Location) where V : BitwiseCopyable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/setuniformvalue(_:at:))*