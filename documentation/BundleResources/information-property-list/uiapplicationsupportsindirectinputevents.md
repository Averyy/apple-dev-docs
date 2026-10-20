# UIApplicationSupportsIndirectInputEvents

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value indicating that the app generally supports indirect input mechanisms.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- visionOS 1.0+

## Details

- **Name**: `UIApplicationSupportsIndirectInputEvents` (Application supports indirect input events)
- **Type**: boolean

#### Discussion

If the value of this key is `YES`:

- When the user clicks an indirect pointing device, UIKit generates a [`UITouch`](../../UIKit/uitouch.md) of type [`UITouch.TouchType.indirectPointer`](../../UIKit/uitouch/touchtype/indirectpointer.md).
- When pinching or rotating using an indirect touch surface, UIKit drives [`UIPinchGestureRecognizer`](../../UIKit/uipinchgesturerecognizer.md) and [`UIRotationGestureRecognizer`](../../UIKit/uirotationgesturerecognizer.md) with an event of type [`UIEvent.EventType.transform`](../../UIKit/uievent/eventtype/transform.md).
- Currently, only certain prepackaged gestures in UIKit, like [`UIPinchGestureRecognizer`](../../UIKit/uipinchgesturerecognizer.md) and [`UIRotationGestureRecognizer`](../../UIKit/uirotationgesturerecognizer.md), are capable of handling this event. Other gestures may be added to this list in future releases.
- Gestures that may have worked previously with the simulated touches no longer work.
- Be careful with certain [`UIGestureRecognizer`](../../UIKit/uigesturerecognizer.md) APIs when gestures are driven by events of type [`UIEvent.EventType.scroll`](../../UIKit/uievent/eventtype/scroll.md) or [`UIEvent.EventType.transform`](../../UIKit/uievent/eventtype/transform.md).[`numberOfTouches`](../../UIKit/uigesturerecognizer/numberoftouches.md) returns `0`, and` `[`location(ofTouch:in:)`](../../UIKit/uigesturerecognizer/location%28oftouch,in%29.md) raises an exception because there are no touches driving these gestures with those events. For the case when exceptions might be raised, use either [`shouldReceive(_:)`](../../UIKit/uigesturerecognizer/shouldreceive%28_%29.md) or the delegate call of [`gestureRecognizer(_:shouldReceive:)`](../../UIKit/uigesturerecognizerdelegate/gesturerecognizer%28_,shouldreceive%29-evxd.md) to determine that gesture recognizers are acting on a non-touch-based event.

If the value of this key is `NO`:

- When the user clicks an indirect pointing device, UIKit generates a [`UITouch`](../../UIKit/uitouch.md) of type [`UITouch.TouchType.direct`](../../UIKit/uitouch/touchtype/direct.md).
- When pinching or rotating using an indirect touch surface, UIKit creates touches a fixed distance apart that simulate the gesture on the indirect touch surface.
- Because these are normal [`UITouch`](../../UIKit/uitouch.md) events, they may incidentally activate other gesture recognizers

If you *don’t* include this key in your app’s `Info.plist`:

- In iOS 17 and later, the system defaults to supporting indirect input events, meaning it treats your app the same as if you specify `YES`.
- In versions of iOS earlier than iOS 17, the system defaults to not supporting indirect input events, meaning it treats your app the same as if you specify `NO`.

> ❗ **Important**:  [`UIApplicationSupportsIndirectInputEvents`](./uiapplicationsupportsindirectinputevents.md) is a compatibility affordance to ease the adoption of indirect input for a UIKit application. Avoid relying on this property and prepare your app to support indirect gestures on all platforms. For visionOS, the system always supports indirect input events and doesn’t consult this key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationsupportsindirectinputevents)*