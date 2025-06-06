# ARView.RenderOptions.Element

**Framework**: RealityKit  
**Kind**: typealias

The element type of the option set.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
typealias Element = ARView.RenderOptions
```

#### Discussion

To inherit all the default implementations from the `OptionSet` protocol, the `Element` type must be `Self`, the default.

## See Also

- [init()](arview/renderoptions-swift.struct/init.md)
  Creates an empty option set.
- [init<S>(S)](arview/renderoptions-swift.struct/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](arview/renderoptions-swift.struct/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [ARView.RenderOptions.ArrayLiteralElement](arview/renderoptions-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: UInt)](arview/renderoptions-swift.struct/init(rawvalue:).md)
  Creates a new option set from the given raw value.
- [ARView.RenderOptions.RawValue](arview/renderoptions-swift.struct/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [let rawValue: UInt](arview/renderoptions-swift.struct/rawvalue-swift.property.md)
  The corresponding value of the raw type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/renderoptions-swift.struct/element)*