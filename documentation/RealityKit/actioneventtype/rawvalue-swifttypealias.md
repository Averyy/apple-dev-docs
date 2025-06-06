# ActionEventType.RawValue

**Framework**: RealityKit  
**Kind**: typealias

The raw type that can be used to represent all values of the conforming type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
typealias RawValue = UInt
```

#### Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.

## See Also

- [init(rawValue: UInt)](actioneventtype/init(rawvalue:).md)
  Creates an action event type from a raw value.
- [let rawValue: UInt](actioneventtype/rawvalue-swift.property.md)
  The backing storage for action event types.
- [ActionEventType.ArrayLiteralElement](actioneventtype/arrayliteralelement.md)
  The type of the elements of an array literal.
- [ActionEventType.Element](actioneventtype/element.md)
  The element type of the option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actioneventtype/rawvalue-swift.typealias)*