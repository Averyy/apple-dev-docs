# init(view:)

**Framework**: UIKit  
**Kind**: init

Returns a newly initialized preview interaction for the specified view.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(view: UIView)
```

#### Return Value

An initialized preview interaction.

#### Discussion

Preview interactions operate on touches within a specified view. Unlike gesture recognizers, the view doesn’t maintain a strong reference to preview interactions. You must therefore retain a reference to the preview interaction to ensure that it continues to receive touches from the view.

## Parameters

- `view`: The view for which the preview interaction should respond.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewinteraction/init(view:))*