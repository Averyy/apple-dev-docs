# FormatInput

**Framework**: Foundation  
**Kind**: associatedtype  
**Required**: Yes

The type this format style accepts as input.

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
associatedtype FormatInput
```

#### Discussion

Swift type inference uses this value to determine which static accessors are available at a given call point. For example, when you format an [`Int32`](https://developer.apple.com/documentation/Swift/Int32), you can use the static [`number`](formatstyle/number-4cj49.md) property that provies a `IntegerFormatStyle<Int32>`, as seen in the following example. This works because the style’s input type `IntegerFormatStyle/FormatInput` is a [`BinaryInteger`](https://developer.apple.com/documentation/Swift/BinaryInteger) generically constrained to the [`Int32`](https://developer.apple.com/documentation/Swift/Int32) type.

```swift
let perihelionDistanceToSunInKm: Int32 = 147098291
perihelionDistanceToSunInKm.formatted(.number
    .notation(.scientific)) // "1.470983E8"
```

## See Also

- [associatedtype FormatOutput](formatstyle/formatoutput.md)
  The type this format style produces as output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/formatinput)*