# percent

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A style for formatting decimal values as a percent representation.

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
static var percent: Decimal.FormatStyle.Percent { get }
```

Available when `Self` is `Decimal.FormatStyle.Percent`.

## Discussion

Use this type property when the call point allows the use of [`Decimal.FormatStyle`](../decimal/formatstyle.md). You typically do this when calling the [`formatted(_:)`](../decimal/formatted%28_%29.md) method of [`Decimal`](../decimal.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/parseableformatstyle/percent)*