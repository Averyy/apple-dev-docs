# touchedInput

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The input object that provides the touch state of the element.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var touchedInput: (any GCTouchedStateInput)? { get }
```

```objc
@property (readonly, nullable) id<GCTouchedStateInput> touchedInput;
```

## See Also

### Getting input state
- [var pressedInput: any GCLinearInput & GCPressedStateInput](./pressedinput.md)
  The input object that provides the linear and press state of the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcbuttonelement/touchedinput)*