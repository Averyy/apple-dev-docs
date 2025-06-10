# PresentationCommandType

**Framework**: Immersive Media Support  
**Kind**: enum

Values that represent the type of presentation command.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum PresentationCommandType
```

## Topics

### Enumeration Cases
- [PresentationCommandType.fade](presentationcommandtype/fade.md)
  A fade command used during scene transitions. This command adds a fade in / fade out during playback.
- [PresentationCommandType.fadeEnvironment](presentationcommandtype/fadeenvironment.md)
  The environment fade command is used during backdrop transitions. This command adds a fade in / fade out for the backdrop during playback.
- [PresentationCommandType.setCamera](presentationcommandtype/setcamera.md)
  setCamera specifies the camera ID to be used for a specific frame during playback.
- [PresentationCommandType.shotFlop](presentationcommandtype/shotflop.md)
  A shotFlop command will cause the whole frame to be mirrored horizontally for the duration of the command.
### Initializers
- [init?(intValue: Int)](presentationcommandtype/init(intvalue:).md)
  Creates a new instance from the specified integer.
- [init?(rawValue: String)](presentationcommandtype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [init?(stringValue: String)](presentationcommandtype/init(stringvalue:).md)
  Creates a new instance from the given string.
### Instance Properties
- [var intValue: Int?](presentationcommandtype/intvalue.md)
  The value to use in an integer-indexed collection (e.g. an int-keyed dictionary).
- [var rawValue: String](presentationcommandtype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [var stringValue: String](presentationcommandtype/stringvalue.md)
  The string to use in a named collection (e.g. a string-keyed dictionary).
### Type Aliases
- [PresentationCommandType.AllCases](presentationcommandtype/allcases-swift.typealias.md)
  A type that can represent a collection of all values of this type.
- [PresentationCommandType.RawValue](presentationcommandtype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static var allCases: [PresentationCommandType]](presentationcommandtype/allcases-swift.type.property.md)
  A collection of all values of this type.
### Default Implementations
- [CodingKey Implementations](presentationcommandtype/codingkey-implementations.md)
- [Equatable Implementations](presentationcommandtype/equatable-implementations.md)
- [RawRepresentable Implementations](presentationcommandtype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [CodingKey](../Swift/CodingKey.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol PresentationCommand](presentationcommand.md)
  A set of properties that define the interface for a presentation command.
- [struct FadeCommand](fadecommand.md)
  A command type for color fading during immersive media playback.
- [struct FadeEnvironmentCommand](fadeenvironmentcommand.md)
  A command type for opacity fading environment backdrops during immersive media playback.
- [struct SetCameraCommand](setcameracommand.md)
  A command type for immersive camera switching during playback.
- [struct ShotFlopCommand](shotflopcommand.md)
  A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- [struct PresentationDescriptor](presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [class PresentationDescriptorReader](presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationcommandtype)*