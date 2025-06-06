# isPINFallback

**Framework**: ProximityReader  
**Kind**: property

A Boolean value that indicates whether the PIN Fallback occurred.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
let isPINFallback: Bool
```

#### Discussion

When the framework sets this property to `true`, the `paymentCardData` is a PIN Fallback read.

## See Also

- [let pinBypassed: Bool](paymentcardreadresult/pinbypassed.md)
  A Boolean value that indicates whether the consumer bypassed the PIN entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult/ispinfallback)*