# delegate

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

A delegate that responds to the scroll view’s scroll updates.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
weak var delegate: (any BEScrollViewDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<BEScrollViewDelegate> delegate;
```

## Discussion

`BEScrollView` doesn’t retain the delegate, which must conform to the [`BEScrollViewDelegate`](../bescrollviewdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollview/delegate)*