# rawValue

**Framework**: RealityKit  
**Kind**: property

The corresponding value of the raw type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS ?+

## Declaration

```swift
var rawValue: String { get }
```

#### Discussion

A new instance initialized with `rawValue` will be equivalent to this instance. For example:

```None
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

let selectedSize = PaperSize.Letter
print(selectedSize.rawValue)
// Prints "Letter"

print(selectedSize == PaperSize(rawValue: selectedSize.rawValue)!)
// Prints "true"
```

## See Also

- [init?(rawValue: String)](modeldebugoptionscomponent/visualizationmode-swift.enum/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [ModelDebugOptionsComponent.VisualizationMode.RawValue](modeldebugoptionscomponent/visualizationmode-swift.enum/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modeldebugoptionscomponent/visualizationmode-swift.enum/rawvalue-swift.property)*