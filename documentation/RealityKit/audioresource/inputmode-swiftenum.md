# AudioResource.InputMode

**Framework**: RealityKit  
**Kind**: enum

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
enum InputMode
```

## Topics

### Input modes
- [AudioResource.InputMode.nonSpatial](audioresource/inputmode-swift.enum/nonspatial.md)
  the input channels are mixed to whatever the output format is without any spatialization
- [AudioResource.InputMode.spatial](audioresource/inputmode-swift.enum/spatial.md)
  a spatialized with all degrees of freedom. This treats a resource as a mono stream so mixes all its channels to mono
- [AudioResource.InputMode.ambient](audioresource/inputmode-swift.enum/ambient.md)
  spatialized but ignores listener translation and only follows listener head rotation
### Comparing input modes
- [static func == (AudioResource.InputMode, AudioResource.InputMode) -> Bool](audioresource/inputmode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](audioresource/inputmode-swift.enum/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](audioresource/inputmode-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](audioresource/inputmode-swift.enum/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](audioresource/inputmode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var inputMode: AudioResource.InputMode](audioresource/inputmode-swift.property.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioresource/inputmode-swift.enum)*