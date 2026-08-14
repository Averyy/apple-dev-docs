# parentScrollView(for:)

**Framework**: BrowserEngineKit  
**Kind**: method

Returns the scroll view that acts as the DOM container of the given scroll view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
optional func parentScrollView(for scrollView: BEScrollView) -> BEScrollView?
```

#### Return Value

The scroll view that is the logical DOM container of the provided scroll view. Return `nil` to get the default behavior, where the system recursively searches the scroll view’s [`superview`](https://developer.apple.com/documentation/uikit/uiview/superview) hierarchy for a containing scroll view.

#### Discussion

To correctly render some websites, you may need to create [`BEScrollView`](bescrollview.md) objects that are siblings in the view hierarchy but nested in the DOM. In these situations, implement this method in the delegate of the logically contained scroll view, and return the logically containing scroll view. The containing scroll view must appear visually beneath the contained scroll view.

## Parameters

- `scrollView`: The scroll view for which to return the logically containing scroll view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewdelegate/parentscrollview(for:))*