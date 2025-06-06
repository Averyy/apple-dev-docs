# init(signedArchive:onCompletion:)

**Framework**: FinanceKitUI  
**Kind**: init

Returns an initialized Add to Order Button.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
@MainActor
@preconcurrency init(signedArchive: Data, onCompletion: @escaping (Result<FinanceStore.SaveOrderResult, any Error>) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/init(signedarchive:oncompletion:))*