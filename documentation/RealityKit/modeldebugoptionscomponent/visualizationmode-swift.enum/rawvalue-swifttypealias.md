# ModelDebugOptionsComponent.VisualizationMode.RawValue

**Framework**: RealityKit  
**Kind**: typealias

The raw type that can be used to represent all values of the conforming type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
typealias RawValue = String
```

#### Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.

## See Also

- [init?(rawValue: String)](modeldebugoptionscomponent/visualizationmode-swift.enum/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: String](modeldebugoptionscomponent/visualizationmode-swift.enum/rawvalue-swift.property.md)
  The corresponding value of the raw type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modeldebugoptionscomponent/visualizationmode-swift.enum/rawvalue-swift.typealias)*