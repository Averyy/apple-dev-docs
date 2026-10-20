# MLImageSizeConstraintType

**Framework**: Core ML  
**Kind**: enum  
**Role**: Enumeration

The modes that determine how the model defines a feature’s image size constraint.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum MLImageSizeConstraintType
```

```c
enum MLImageSizeConstraintType : NSInteger;
```

## Topics

### Constraint types
- [MLImageSizeConstraintType.range](./mlimagesizeconstrainttype/range.md)
  The image feature accepts image sizes defined by a range of widths and a range of heights.
- [MLImageSizeConstraintType.enumerated](./mlimagesizeconstrainttype/enumerated.md)
  The image feature accepts image sizes listed in an array.
- [MLImageSizeConstraintType.unspecified](./mlimagesizeconstrainttype/unspecified.md)
  The image size constraint is not configured and should be ignored.
### Creating a constraint type
- [init?(rawValue: Int)](./mlimagesizeconstrainttype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Determining relevant constraints
- [var type: MLImageSizeConstraintType](./mlimagesizeconstraint/type.md)
  Indicator of which properties to inspect for this image size constraint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlimagesizeconstrainttype)*