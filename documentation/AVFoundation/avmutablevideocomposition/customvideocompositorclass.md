# customVideoCompositorClass

**Framework**: AVFoundation  
**Kind**: property

The custom compositor class to use.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var customVideoCompositorClass: (any AVVideoCompositing.Type)? { get set }
```

#### Discussion

The default value is `nil`, indicating that the internal video compositor is used


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/customvideocompositorclass)*