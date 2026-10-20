# NSDecimalIsNotANumber(_:)

**Framework**: Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean that indicates whether a given decimal contains a valid number.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func NSDecimalIsNotANumber(_ dcm: UnsafePointer<Decimal>) -> Bool
```

```c
static BOOL NSDecimalIsNotANumber(const NSDecimal *dcm);
```

#### Return Value

[`false`](../Swift/false.md) if the value in `dcm` represents a valid number, otherwise [`true`](../Swift/true.md).

#### Discussion

For more information, see [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdecimalisnotanumber(_:))*