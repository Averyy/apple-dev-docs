# format(_:)

**Framework**: Foundation  
**Kind**: method

Formats a byte count measurment, using this style.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func format(_ value: Measurement<UnitInformationStorage>) -> String
```

#### Return Value

A formatted representation of `value`, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple values. The following example creates a [`Measurement.FormatStyle.ByteCount`](measurement/formatstyle/bytecount.md) instance to format values as kilobyte counts, then applies this style to an array of [`Measurement`](measurement.md) values.

```swift
let style = Measurement.FormatStyle.ByteCount(style: .memory,                                              
                                              allowedUnits: [.kb],
                                              spellsOutZero: true,
                                              includesActualByteCount: false,
                                              locale: Locale(identifier: "en_US"))
let counts: [Measurement] = [
    Measurement(value: 0, unit: UnitInformationStorage.bytes),
    Measurement(value: 1024, unit: UnitInformationStorage.bytes),
    Measurement(value: 2048, unit: UnitInformationStorage.bytes),
    Measurement(value: 4096, unit: UnitInformationStorage.bytes),
    Measurement(value: 8192, unit: UnitInformationStorage.bytes),
    Measurement(value: 16384, unit: UnitInformationStorage.bytes),
    Measurement(value: 32768, unit: UnitInformationStorage.bytes),
    Measurement(value: 65536, unit: UnitInformationStorage.bytes)
]
let formatted = counts.map ( {style.format($0) } ) // ["Zero kB", "1 kB", "2 kB", "4 kB", "8 kB", "16 kB", "32 kB", "64 kB"]
```

To format a single data-storage measurement, use the Measurement instance method [`formatted(_:)`](measurement/formatted(_:).md), passing in an instance of [`Measurement.FormatStyle.ByteCount`](measurement/formatstyle/bytecount.md), or [`formatted()`](measurement/formatted().md) to use a default style.

## Parameters

- `value`: The byte count measurement to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/bytecount/format(_:))*