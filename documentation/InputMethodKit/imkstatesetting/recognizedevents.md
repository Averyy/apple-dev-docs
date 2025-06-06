# recognizedEvents(_:)

**Framework**: InputMethodKit  
**Kind**: method  
**Required**: Yes

Returns an unsigned integer that contains a union of event masks

**Availability**:
- macOS 10.5+

## Declaration

```swift
func recognizedEvents(_ sender: Any!) -> Int
```

#### Return Value

An unsigned integer that contains a union of event masks (See the `NSEvent.h` header file.

#### Discussion

A client calls this method to check whether an input method supports an event. The default implementation returns `NSKeyDownMask`. If your input method handles only key down events, the Input Method Kit provides the default mouse handling. The default mouse-down handling behavior is as follows: If there is an active composition area and the user clicks in the text but outside of the composition area, the Input Method Kit sends your input method a `commitComposition:` message. This happens only for input methods that return only the default value—`NSKeyDownMask`.

## Parameters

- `sender`: The client object requesting the supported events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting/recognizedevents(_:))*