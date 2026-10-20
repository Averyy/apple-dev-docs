# pressedInput

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The input object that provides the linear and press state of the element.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var pressedInput: any GCLinearInput & GCPressedStateInput { get }
```

```objc
@property (readonly) id<GCLinearInput,GCPressedStateInput> pressedInput;
```

## Mentions

- [Handling input events](../handling-input-events.md)

## See Also

### Getting input state
- [var touchedInput: (any GCTouchedStateInput)?](./touchedinput.md)
  The input object that provides the touch state of the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcbuttonelement/pressedinput)*