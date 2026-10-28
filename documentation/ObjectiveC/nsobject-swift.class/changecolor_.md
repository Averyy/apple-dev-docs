# changeColor:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Sent to the first responder when the user selects a color in an `NSColorPanel` object.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (void) changeColor:(id) sender;
```

## Discussion

When the user selects a color in an [`NSColorPanel`](../../AppKit/nscolorpanel.md) object, the panel tries to call this method on the first responder. You can override this method in any responder that needs to respond to a color change.

## Parameters

- `sender`: The `NSColorPanel` sending the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/changecolor:)*