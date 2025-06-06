# callAsFunction(_:)

**Framework**: StoreKit  
**Kind**: method

Tells StoreKit to display the App Store message, if appropriate.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func callAsFunction(_ message: Message) throws
```

#### Discussion

Don’t call this method directly. SwiftUI calls it when you call the [`DisplayMessageAction`](displaymessageaction.md) structure using `message` as an argument.

For information about how Swift uses the [`callAsFunction()`](requestreviewaction/callasfunction().md) method to simplify call site syntax, see [`Methods with Special Names`](https://developer.apple.comhttps://docs.swift.org/swift-book/ReferenceManual/Declarations.html#ID622) in .

## Parameters

- `message`: The App Store message to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/displaymessageaction/callasfunction(_:))*