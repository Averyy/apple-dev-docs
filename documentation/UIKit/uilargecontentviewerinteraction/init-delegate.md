# init(delegate:)

**Framework**: UIKit  
**Kind**: init

Creates an interaction object with the specified delegate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(delegate: (any UILargeContentViewerInteractionDelegate)?)
```

#### Discussion

To add the interaction to a view, use [`addInteraction(_:)`](uiview/addinteraction(_:).md).

## Parameters

- `delegate`: An object that implements the   protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilargecontentviewerinteraction/init(delegate:))*