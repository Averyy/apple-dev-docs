# ActionEventType.Element

**Framework**: RealityKit  
**Kind**: typealias

The element type of the option set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
typealias Element = ActionEventType
```

#### Discussion

To inherit all the default implementations from the `OptionSet` protocol, the `Element` type must be `Self`, the default.

## See Also

- [init(rawValue: UInt)](actioneventtype/init(rawvalue:).md)
  Creates an action event type from a raw value.
- [let rawValue: UInt](actioneventtype/rawvalue-swift.property.md)
  The backing storage for action event types.
- [ActionEventType.ArrayLiteralElement](actioneventtype/arrayliteralelement.md)
  The type of the elements of an array literal.
- [ActionEventType.RawValue](actioneventtype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actioneventtype/element)*