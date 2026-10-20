# AxisTick.Length

**Framework**: Swift Charts  
**Kind**: struct  
**Role**: Structure

Describes the length of a tick.

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
struct Length
```

## Topics

### Type Properties
- [static var automatic: AxisTick.Length](./length/automatic.md)
  Automatically determines the tick length.
- [static var label: AxisTick.Length](./length/label.md)
  Describes a tick that extends to its associated label.
- [static var longestLabel: AxisTick.Length](./length/longestlabel.md)
  Describes a tick that extends to the longest label on the axis.
### Type Methods
- [static func label(extendPastBy: CGFloat) -> AxisTick.Length](./length/label%28extendpastby%29.md)
  Describes a tick that extends to its associated label, with the given additional length.
- [static func longestLabel(extendPastBy: CGFloat) -> AxisTick.Length](./length/longestlabel%28extendpastby%29.md)
  Describes a tick that extends to the longest label on the axis, with the given additional length.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axistick/length)*