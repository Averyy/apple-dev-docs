# valueChangedHandler

**Framework**: Game Controller  
**Kind**: property

The block that the directional pad calls when the user changes its values.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var valueChangedHandler: GCControllerDirectionPadValueChangedHandler? { get set }
```

#### Discussion

Set this handler to receive notifications when the user changes a direction value.

## See Also

- [typealias GCControllerDirectionPadValueChangedHandler](gccontrollerdirectionpadvaluechangedhandler.md)
  The signature for the block that executes when either axis changes values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerdirectionpad/valuechangedhandler)*