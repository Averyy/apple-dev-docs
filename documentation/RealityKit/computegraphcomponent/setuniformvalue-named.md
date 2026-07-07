# setUniformValue(_:named:)

**Framework**: RealityKit  
**Kind**: method

Sets the value of a named uniform to a `BitwiseCopyable` typed value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@discardableResult
mutating func setUniformValue<V>(_ value: V, named name: String) -> Bool where V : BitwiseCopyable
```

#### Return Value

`true` if the uniform was found and updated; `false` otherwise.

## Parameters

- `value`: The value to write.
- `name`: The name of the uniform to update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/setuniformvalue(_:named:))*