# CustomerEngagementSession.ConsentOption.preSelected

**Framework**: ProximityReader  
**Kind**: case  
**Role**: Case

Shows the customer the receive promotions option with a default preference.

**Availability**:
- iOS 27.0+ - Deprecated in 27.2
- iPadOS 27.0+ - Deprecated in 27.2
- Mac Catalyst 27.0+

> **Deprecated**: Use .visible instead; consent is never pre-selected

## Declaration

```swift
case preSelected
```

## Discussion

> ⚠️ **Warning**: Deprecated. Pre-selecting consent is no longer supported; this behaves the same as [`CustomerEngagementSession.ConsentOption.visible`](./visible.md) and shows the option with nothing selected, so the customer always makes an explicit choice.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/consentoption/preselected)*