# handlingWriting

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the user is actively writing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```objc
@property (nonatomic, readonly, getter=isHandlingWriting) BOOL handlingWriting;
```

## Discussion

Set to [`true`](../../Swift/true.md) in between calls to [`indirectScribbleInteraction:willBeginWritingInElement:`](../uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_willbeginwritinginelement_.md) and [`indirectScribbleInteraction:didFinishWritingInElement:`](../uiindirectscribbleinteractiondelegate-3jmnk/indirectscribbleinteraction_didfinishwritinginelement_.md) calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiindirectscribbleinteraction-2dap8/handlingwriting)*