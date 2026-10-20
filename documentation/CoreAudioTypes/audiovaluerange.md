# AudioValueRange

**Framework**: Core Audio Types  
**Kind**: struct  
**Role**: Structure

A structure that represents a continuous range of values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioValueRange
```

```c
struct AudioValueRange;
```

## Topics

### Inspecting a range
- [var mMaximum: Float64](./audiovaluerange/mmaximum.md)
  The maximum value.
- [var mMinimum: Float64](./audiovaluerange/mminimum.md)
  The minimum value.
### Initializers
- [init()](./audiovaluerange/init%28%29.md)
- [init(mMinimum: Float64, mMaximum: Float64)](./audiovaluerange/init%28mminimum,mmaximum%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Values
- [struct AudioValueTranslation](./audiovaluetranslation.md)
  A structure that stores buffers to use in translation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiovaluerange)*