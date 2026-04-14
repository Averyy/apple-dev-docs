# scrollView(_:handle:completion:)

**Framework**: BrowserEngineKit  
**Kind**: method

Handles a scroll update before the scroll view reacts to it.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func scrollView(_ scrollView: BEScrollView, handle scrollUpdate: BEScrollViewScrollUpdate) async -> Bool
```

#### Discussion

Your `BEScrollViewDelegate` receives scroll updates before its delegating scroll view handles them. The system calls this method on the main queue — retrieve information from `scrollUpdate` on the main queue, then process the update asynchronously. Call the `completion` block asynchronously on the main queue when you finish processing.

> ❗ **Important**:  Call completion blocks on the main queue in the same order in which you receive scroll updates.

## Parameters

- `scrollView`: The [`BEScrollView`](bescrollview.md) that receives the scroll update.
- `scrollUpdate`: An object that describes the scroll update. Retrieve all information from this object immediately on the main queue when the system calls your delegate method, as the values may change.
- `completion`: A block to call when you finish processing the scroll update. Pass `true` if you handled the scroll event and the scroll view doesn’t need to react to it; pass `false` otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewdelegate/scrollview(_:handle:completion:))*