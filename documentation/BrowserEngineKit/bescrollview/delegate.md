# delegate

**Framework**: BrowserEngineKit  
**Kind**: property

The delegate of the scroll view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
weak var delegate: (any BEScrollViewDelegate)? { get set }
```

#### Overview

The `BEScrollView` class doesn’t retain the delegate, which must conform to the [`BEScrollViewDelegate`](bescrollviewdelegate.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollview/delegate)*