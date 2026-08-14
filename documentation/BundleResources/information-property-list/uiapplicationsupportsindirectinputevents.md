# UIApplicationSupportsIndirectInputEvents

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value indicating that the app generally supports indirect input mechanisms.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- visionOS 1.0+



**Type**: boolean

#### Discussion

If the value of this key is `YES`:

- When the user clicks an indirect pointing device, UIKit generates a [`UITouch`](https://developer.apple.com/documentation/uikit/uitouch) of type [`UITouch.TouchType.indirectPointer`](https://developer.apple.com/documentation/uikit/uitouch/touchtype/indirectpointer).
- When pinching or rotating using an indirect touch surface, UIKit drives [`UIPinchGestureRecognizer`](https://developer.apple.com/documentation/uikit/uipinchgesturerecognizer) and [`UIRotationGestureRecognizer`](https://developer.apple.com/documentation/uikit/uirotationgesturerecognizer) with an event of type [`UIEvent.EventType.transform`](https://developer.apple.com/documentation/uikit/uievent/eventtype/transform).
- Currently, only certain prepackaged gestures in UIKit, like [`UIPinchGestureRecognizer`](https://developer.apple.com/documentation/uikit/uipinchgesturerecognizer) and [`UIRotationGestureRecognizer`](https://developer.apple.com/documentation/uikit/uirotationgesturerecognizer), are capable of handling this event. Other gestures may be added to this list in future releases.
- Gestures that may have worked previously with the simulated touches no longer work.
- Be careful with certain [`UIGestureRecognizer`](https://developer.apple.com/documentation/uikit/uigesturerecognizer) APIs when gestures are driven by events of type [`UIEvent.EventType.scroll`](https://developer.apple.com/documentation/uikit/uievent/eventtype/scroll) or [`UIEvent.EventType.transform`](https://developer.apple.com/documentation/uikit/uievent/eventtype/transform).[`numberOfTouches`](https://developer.apple.com/documentation/uikit/uigesturerecognizer/numberoftouches) returns `0`, and` `[`location(ofTouch:in:)`](https://developer.apple.com/documentation/uikit/uigesturerecognizer/location(oftouch:in:)) raises an exception because there are no touches driving these gestures with those events. For the case when exceptions might be raised, use either [`shouldReceive(_:)`](https://developer.apple.com/documentation/uikit/uigesturerecognizer/shouldreceive(_:)) or the delegate call of [`gestureRecognizer(_:shouldReceive:)`](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldreceive:)-evxd) to determine that gesture recognizers are acting on a non-touch-based event.

If the value of this key is `NO`:

- When the user clicks an indirect pointing device, UIKit generates a [`UITouch`](https://developer.apple.com/documentation/uikit/uitouch) of type [`UITouch.TouchType.direct`](https://developer.apple.com/documentation/uikit/uitouch/touchtype/direct).
- When pinching or rotating using an indirect touch surface, UIKit creates touches a fixed distance apart that simulate the gesture on the indirect touch surface.
- Because these are normal [`UITouch`](https://developer.apple.com/documentation/uikit/uitouch) events, they may incidentally activate other gesture recognizers

If you *don’t* include this key in your app’s `Info.plist`:

- In iOS 17 and later, the system defaults to supporting indirect input events, meaning it treats your app the same as if you specify `YES`.
- In versions of iOS earlier than iOS 17, the system defaults to not supporting indirect input events, meaning it treats your app the same as if you specify `NO`.

> ❗ **Important**:  [`UIApplicationSupportsIndirectInputEvents`](information-property-list/uiapplicationsupportsindirectinputevents.md) is a compatibility affordance to ease the adoption of indirect input for a UIKit application. Avoid relying on this property and prepare your app to support indirect gestures on all platforms. For visionOS, the system always supports indirect input events and doesn’t consult this key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationsupportsindirectinputevents)*