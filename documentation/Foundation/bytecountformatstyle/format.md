# format(_:)

**Framework**: Foundation  
**Kind**: method

Formats a numeric byte count, using this style.

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
func format(_ value: Int64) -> String
```

#### Return Value

A formatted representation of `value`, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple values. The following example creates a [`ByteCountFormatStyle`](bytecountformatstyle.md) to format values as kilobyte counts, then applies this style to an array of [`Int64`](https://developer.apple.com/documentation/swift/int64) values.

```swift
let style = ByteCountFormatStyle(style: .memory,
                                 allowedUnits: [.kb],
                                 spellsOutZero: true,
                                 includesActualByteCount: false,
                                 locale: Locale(identifier: "en_US"))
let counts: [Int64] = [0, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
let formatted = counts.map ( {style.format($0) } ) // ["Zero kB", "1 kB", "2 kB", "4 kB", "8 kB", "16 kB", "32 kB", "64 kB"]

```

To format a single integer, use the [`BinaryInteger`](https://developer.apple.com/documentation/swift/binaryinteger) instance method [`formatted(_:)`](https://developer.apple.com/documentation/swift/binaryinteger/formatted(_:)-4qd73), passing in an instance of [`IntegerFormatStyle`](integerformatstyle.md), or [`formatted()`](https://developer.apple.com/documentation/swift/binaryinteger/formatted()) to use a default style.

## Parameters

- `value`: The 64-bit byte count to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatstyle/format(_:))*