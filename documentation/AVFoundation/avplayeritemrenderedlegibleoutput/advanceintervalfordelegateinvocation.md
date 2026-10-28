# advanceIntervalForDelegateInvocation

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Permits advance invocation of the associated delegate, if any.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
var advanceIntervalForDelegateInvocation: TimeInterval { get set }
```

```objc
@property (nonatomic, readwrite) NSTimeInterval advanceIntervalForDelegateInvocation;
```

## Discussion

Use this property specify the number of seconds early to invoke the delegate object. When possible, an AVPlayerItemLegibleOutput uses this value to call its delegate earlier than it would otherwise.

## See Also

### Configuring an output
- [var videoDisplaySize: CGSize](./videodisplaysize.md)
  Set the video display size to use for rendering of pixel buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput/advanceintervalfordelegateinvocation)*