# validate(completionHandler:)

**Framework**: ARKit  
**Kind**: method

Determines whether the reference image is valid.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func validate() async throws
```

#### Discussion

ARKit considers certain images invalid for image tracking (for example, an image that’s all white). Call this function on a reference image you create programmatically to make sure ARKit can track it, before passing it in to your session’s [`detectionImages`](arworldtrackingconfiguration/detectionimages.md) array.

You only need this function when you create a reference image programmatically, because Xcode performs this validation for you when you create a reference image in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceimage/validate(completionhandler:))*