# up

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The input object that represents the up button on the directional pad.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var up: any GCLinearInput & GCPressedStateInput { get }
```

```objc
@property (readonly) id<GCLinearInput,GCPressedStateInput> up;
```

## See Also

### Directional buttons
- [var left: any GCLinearInput & GCPressedStateInput](./left.md)
  The input object that represents the left button on the directional pad.
- [var right: any GCLinearInput & GCPressedStateInput](./right.md)
  The input object that represents the right button on the directional pad.
- [var down: any GCLinearInput & GCPressedStateInput](./down.md)
  The input object that represents the down button on the directional pad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdirectionpadelement/up)*