# scrollMode

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Defines the axes in which the layer may be scrolled.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var scrollMode: CAScrollLayerScrollMode { get set }
```

```objc
@property (copy) CAScrollLayerScrollMode scrollMode;
```

#### Discussion

The possible values are described in [Scroll Modes](../scroll-modes.md). The default is [`both`](../cascrolllayerscrollmode/both.md).

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cascrolllayer/scrollmode)*