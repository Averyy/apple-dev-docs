# AXNumericDataAxisDescriptor.ScaleType

**Framework**: Accessibility  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the scale of a numeric axis.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum ScaleType
```

```c
enum AXNumericDataAxisDescriptorScale : NSInteger;
```

## Topics

### Scales
- [AXNumericDataAxisDescriptor.ScaleType.linear](./scaletype-swift.enum/linear.md)
  A linear scale.
- [AXNumericDataAxisDescriptor.ScaleType.ln](./scaletype-swift.enum/ln.md)
  A natural log scale.
- [AXNumericDataAxisDescriptor.ScaleType.log10](./scaletype-swift.enum/log10.md)
  A log scale.
### Initializers
- [init?(rawValue: Int)](./scaletype-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the axis scale
- [var scaleType: AXNumericDataAxisDescriptor.ScaleType](./scaletype-swift.property.md)
  The scale for the axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessibility/axnumericdataaxisdescriptor/scaletype-swift.enum)*