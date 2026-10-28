# presentsWithTransaction

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the layer presents its content using a Core Animation transaction.

**Availability**:
- iOS 9.0+ - Deprecated in 12.0
- iPadOS 9.0+ - Deprecated in 12.0
- tvOS 9.0+ - Deprecated in 12.0

## Declaration

```swift
var presentsWithTransaction: Bool { get set }
```

```objc
@property BOOL presentsWithTransaction;
```

## Discussion

By default this value is [`false`](../../Swift/false.md): [`CAEAGLLayer`](../caeagllayer.md) displays the output of a rendering pass to the display as quickly as possible and asynchronously to any Core Animation transactions. However, if your game or app combines OpenGL and Core Animation content, it’s not guaranteed that your OpenGL content will arrive in the same frame as your Core Animation content. This could be an issue if, for example, your app draws [UIKit](https://developer.apple.com/library/archive/releasenotes/General/RN-iOSSDK-6_1/index.html#//apple_ref/doc/uid/TP40012869-CH1-SW17) content (such as labels with a target position and time) over the top of your [`CAEAGLLayer`](../caeagllayer.md) and the two domains need to be synchronized.

Setting this value to [`true`](../../Swift/true.md) changes this default behavior so that your [`CAEAGLLayer`](../caeagllayer.md) displays its drawable content synchronously, using whichever Core Animation transaction is current.

.

## See Also

### Accessing the Layer Properties
- [var drawableProperties: [String : Any]?](../../OpenGLES/eagldrawable/drawableproperties.md)
  A dictionary of values that specify the desired characteristics of the drawable surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caeagllayer/presentswithtransaction)*