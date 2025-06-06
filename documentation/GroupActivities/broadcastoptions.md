# BroadcastOptions

**Framework**: Group Activities  
**Kind**: struct

Options for how to broadcast media on the shared communications channel.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct BroadcastOptions
```

#### Overview

Use these options to alter how the system presents audio and video associated with an activity’s FaceTime call. For example, you might mirror video during a workout activity to make it easier to follow the instructor’s movements.

## Topics

### Getting the broadcast options
- [static let mirroredVideo: BroadcastOptions](broadcastoptions/mirroredvideo.md)
  An option to mirror video on its vertical axis.
### Creating options from a raw value
- [init(rawValue: Int)](broadcastoptions/init(rawvalue:).md)
  Creates a set of options from a raw value.
- [let rawValue: Int](broadcastoptions/rawvalue-swift.property.md)
  The raw value.
### Type Aliases
- [BroadcastOptions.ArrayLiteralElement](broadcastoptions/arrayliteralelement.md)
  The type of the elements of an array literal.
- [BroadcastOptions.Element](broadcastoptions/element.md)
  The element type of the option set.
- [BroadcastOptions.RawValue](broadcastoptions/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](broadcastoptions/equatable-implementations.md)
- [OptionSet Implementations](broadcastoptions/optionset-implementations.md)
- [SetAlgebra Implementations](broadcastoptions/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var supportsContinuationOnTV: Bool](groupactivitymetadata/supportscontinuationontv.md)
  A Boolean value that indicates whether your app supports activity continuation on an Apple TV.
- [var preferredBroadcastOptions: BroadcastOptions](groupactivitymetadata/preferredbroadcastoptions.md)
  Preferences for how to present audio and video on the main communication channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/broadcastoptions)*