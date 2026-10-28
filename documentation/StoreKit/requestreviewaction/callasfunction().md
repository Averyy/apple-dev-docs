# callAsFunction()

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Tells StoreKit to ask the user to rate or review your app, if appropriate.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func callAsFunction()
```

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`RequestReviewAction`](../requestreviewaction.md) instance that you get from the [`requestReview`](../../SwiftUI/environmentvalues/requestreview.md) environment value.

For information about how Swift uses the [`callAsFunction()`](./callasfunction%28%29.md)method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in *The Swift Programming Language*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/requestreviewaction/callasfunction())*