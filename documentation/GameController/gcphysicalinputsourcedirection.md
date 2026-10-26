# GCPhysicalInputSourceDirection

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

The directions that a physical input source involves.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct GCPhysicalInputSourceDirection
```

```c
enum GCPhysicalInputSourceDirection : NSUInteger;
```

## Topics

### Directions
- [static var up: GCPhysicalInputSourceDirection](./gcphysicalinputsourcedirection/up.md)
  The physical input source contains a value for the up direction.
- [static var right: GCPhysicalInputSourceDirection](./gcphysicalinputsourcedirection/right.md)
  The physical input source supports the right direction.
- [static var down: GCPhysicalInputSourceDirection](./gcphysicalinputsourcedirection/down.md)
  The physical input source supports the down direction.
- [static var left: GCPhysicalInputSourceDirection](./gcphysicalinputsourcedirection/left.md)
  The physical input source supports the left direction.
- [GCPhysicalInputSourceDirectionNotApplicable](./gcphysicalinputsourcedirection/gcphysicalinputsourcedirectionnotapplicable.md)
  The physical input source doesn’t support directions.
### Creating the supported directions
- [init(rawValue: UInt)](./gcphysicalinputsourcedirection/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Getting directions
- [var direction: GCPhysicalInputSourceDirection](./gcphysicalinputsource/direction.md)
  The directional input, if any, that a physical input source involves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcphysicalinputsourcedirection)*