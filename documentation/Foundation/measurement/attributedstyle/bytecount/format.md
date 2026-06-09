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
func format(_ value: Measurement<UnitInformationStorage>) -> AttributedString
```

#### Return Value

A formatted representation of `value`, formatted according to the style’s configuration.

#### Discussion

Use this method when you want to create a single style instance, and then use it to format multiple values.

## Parameters

- `value`: The byte count measurement to format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/attributedstyle/bytecount/format(_:))*