# presentedTime

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The host time, in seconds, when the drawable was displayed onscreen.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
var presentedTime: CFTimeInterval { get }
```

#### Discussion

Typically, you query this property in a callback method. See [`addPresentedHandler(_:)`](mtldrawable/addpresentedhandler(_:).md).

The property value is `0.0` if the drawable hasn’t been presented or if its associated frame was dropped.

## See Also

- [func addPresentedHandler(MTLDrawablePresentedHandler)](mtldrawable/addpresentedhandler(_:).md)
  Registers a block of code to be called immediately after the drawable is presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawable/presentedtime)*