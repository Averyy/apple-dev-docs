# takeObjectValueFrom(_:)

**Framework**: AppKit  
**Kind**: method

Sets the value of the receiver’s cell to the object value obtained from the specified object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func takeObjectValueFrom(_ sender: Any?)
```

#### Discussion

You can use this method to link action messages between controls. It permits one control or cell (`sender`) to affect the value of another control (the receiver) by invoking this method in an action message to the receiver. For example, a text field can be made the target of a slider. Whenever the slider is moved, it sends this message to the text field. The text field then obtains the slider’s value, turns it into a text string, and displays it.

## Parameters

- `sender`: The object from which to take the value. This object must respond to the   property.

## See Also

- [func takeDoubleValueFrom(Any?)](nscontrol/takedoublevaluefrom(_:).md)
  Sets the value of the receiver’s cell to a double-precision floating-point value obtained from the specified object.
- [func takeFloatValueFrom(Any?)](nscontrol/takefloatvaluefrom(_:).md)
  Sets the value of the receiver’s cell to a single-precision floating-point value obtained from the specified object.
- [func takeIntValueFrom(Any?)](nscontrol/takeintvaluefrom(_:).md)
  Sets the value of the receiver’s cell to an integer value obtained from the specified object.
- [func takeIntegerValueFrom(Any?)](nscontrol/takeintegervaluefrom(_:).md)
  Sets the value of the receiver’s cell to an `NSInteger` value obtained from the specified object.
- [func takeStringValueFrom(Any?)](nscontrol/takestringvaluefrom(_:).md)
  Sets the value of the receiver’s cell to the string value obtained from the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrol/takeobjectvaluefrom(_:))*