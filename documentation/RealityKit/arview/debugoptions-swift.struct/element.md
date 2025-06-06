# ARView.DebugOptions.Element

**Framework**: RealityKit  
**Kind**: typealias

The element type of the option set.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
typealias Element = ARView.DebugOptions
```

#### Discussion

To inherit all the default implementations from the `OptionSet` protocol, the `Element` type must be `Self`, the default.

## See Also

- [init()](arview/debugoptions-swift.struct/init.md)
  Creates an empty option set.
- [init<S>(S)](arview/debugoptions-swift.struct/init(_:).md)
  Creates a new set from a finite sequence of items.
- [init(arrayLiteral: Self.Element...)](arview/debugoptions-swift.struct/init(arrayliteral:).md)
  Creates a set containing the elements of the given array literal.
- [ARView.DebugOptions.ArrayLiteralElement](arview/debugoptions-swift.struct/arrayliteralelement.md)
  The type of the elements of an array literal.
- [init(rawValue: Int)](arview/debugoptions-swift.struct/init(rawvalue:).md)
  Create a debug options enumeration from a raw value.
- [let rawValue: Int](arview/debugoptions-swift.struct/rawvalue-swift.property.md)
  Options for drawing overlay content in a scene that aids in debugging the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/debugoptions-swift.struct/element)*