# ImagePlaygroundStyle

**Framework**: Image Playground  
**Kind**: struct

Style options that determine the appearance of generated images.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
struct ImagePlaygroundStyle
```

#### Overview

When you create images programmatically, you can ask the system to create images in a particular style. The generative model takes the requested style option and applies it to the content it generates.

## Topics

### Getting the style options
- [static let animation: ImagePlaygroundStyle](imageplaygroundstyle/animation.md)
  An option that yields animated images.
- [static let illustration: ImagePlaygroundStyle](imageplaygroundstyle/illustration.md)
  An option that yields images in a 2D cartoon style.
- [static let sketch: ImagePlaygroundStyle](imageplaygroundstyle/sketch.md)
  An option that yields images in the style of a hand-drawn sketch.
- [static var all: [ImagePlaygroundStyle]](imageplaygroundstyle/all.md)
  An option that allows the creation of images in any style.
### Getting the style identifier
- [let id: String](imageplaygroundstyle/id-swift.property.md)
  A text-based description of the style option.
### Operators
- [static func == (ImagePlaygroundStyle, ImagePlaygroundStyle) -> Bool](imageplaygroundstyle/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](imageplaygroundstyle/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](imageplaygroundstyle/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](imageplaygroundstyle/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](imageplaygroundstyle/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Aliases
- [ImagePlaygroundStyle.ID](imageplaygroundstyle/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](imageplaygroundstyle/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct ImagePlaygroundConcept](imageplaygroundconcept.md)
  Text elements that specify the content to include in the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imageplayground/imageplaygroundstyle)*