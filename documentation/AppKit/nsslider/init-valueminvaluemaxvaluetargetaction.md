# init(value:minValue:maxValue:target:action:)

**Framework**: AppKit  
**Kind**: init

Creates a continuous horizontal slider that represents values over the specified range.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
convenience init(value: Double, minValue: Double, maxValue: Double, target: Any?, action: Selector?)
```

#### Return Value

An initialized slider control.

## Parameters

- `value`: The initial value displayed by the control.
- `minValue`: The minimum value that the control can represent.
- `maxValue`: The maximum value that the control can represent.
- `target`: The target object that receives action messages from the control.
- `action`: The action message sent by the control.

## See Also

- [convenience init(target: Any?, action: Selector?)](nsslider/init(target:action:).md)
  Creates a continuous horizontal slider whose values range from `0.0` to `1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslider/init(value:minvalue:maxvalue:target:action:))*