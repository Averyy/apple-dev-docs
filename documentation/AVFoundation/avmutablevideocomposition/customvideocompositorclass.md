# customVideoCompositorClass

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The custom compositor class to use.

**Availability**:
- iOS 7.0+ - Deprecated in 26.0
- iPadOS 7.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.9+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0

## Declaration

```swift
var customVideoCompositorClass: (any AVVideoCompositing.Type)? { get set }
```

```objc
@property (nonatomic, retain, nullable) Class<AVVideoCompositing> * customVideoCompositorClass;
```

#### Discussion

The default value is `nil`, indicating that the internal video compositor is used


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablevideocomposition/customvideocompositorclass)*