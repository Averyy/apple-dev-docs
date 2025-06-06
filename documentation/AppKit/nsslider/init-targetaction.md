# init(target:action:)

**Framework**: AppKit  
**Kind**: init

Creates a continuous horizontal slider whose values range from `0.0` to `1.0`.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
convenience init(target: Any?, action: Selector?)
```

#### Return Value

An initialized slider control.

## Parameters

- `target`: The target object that receives action messages from the control.
- `action`: The action message sent by the control.

## See Also

- [Slider Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Slider/Slider.html#//apple_ref/doc/uid/10000025i)
- [convenience init(value: Double, minValue: Double, maxValue: Double, target: Any?, action: Selector?)](nsslider/init(value:minvalue:maxvalue:target:action:).md)
  Creates a continuous horizontal slider that represents values over the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/init(target:action:))*