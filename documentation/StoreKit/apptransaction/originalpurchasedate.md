# originalPurchaseDate

**Framework**: StoreKit  
**Kind**: property

The date the customer originally purchased the app from the App Store.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
let originalPurchaseDate: Date
```

#### Discussion

The original purchase date remains the same, even if the customer deletes and reinstalls the app.

In the sandbox testing environment, the original purchase date is always 2013-08-01 12 AM PDT, which is 1375340400000 milliseconds in UNIX epoch time.

## See Also

- [let preorderDate: Date?](apptransaction/preorderdate.md)
  The date the customer placed an order for the app before it’s available in the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/apptransaction/originalpurchasedate)*