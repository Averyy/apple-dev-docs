# prepare(forDrawingPages:)

**Framework**: UIKit  
**Kind**: method

Prepares the renderer for drawing a range of pages.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func prepare(forDrawingPages range: NSRange)
```

#### Discussion

UIKit calls this method before it requests drawing for a range of pages. You can optionally override this method to perform setup tasks. The default implementation does nothing.

## Parameters

- `range`: A range of pages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintpagerenderer/prepare(fordrawingpages:))*