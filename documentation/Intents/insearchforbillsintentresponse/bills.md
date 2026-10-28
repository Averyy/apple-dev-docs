# bills

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The bills found during the search.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var bills: [INBillDetails]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INBillDetails *> * bills;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INBillDetails *> * bills;
```

## Discussion

Use this property to specify the search results. Each [`INBillDetails`](../inbilldetails.md) object should contain information about a single bill that matches the search criteria. Always provide as much detail as possible in each [`INBillDetails`](../inbilldetails.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforbillsintentresponse/bills)*