# Getting high-fidelity input with coalesced touches

**Framework**: UIKit

Learn how to support high-precision touches in your app.

#### Overview

UIKit usually delivers touches to your app at around 60 Hz, but some devices are capable of recording touch information at up to 240 Hz. On such devices, UIKit doesn’t deliver the extra touch information automatically, in case the app doesn’t need the extra data. Instead, it coalesces any extra touches into a single [`UITouch`](uitouch.md) object, whose location reflects only the last recorded touch. However, apps that want the extra precision can retrieve and use the additional touch information.

> ❗ **Important**:  Coalesced touches are intended for apps that need the extra precision and can handle the associated costs. Processing coalesced touches means gathering additional data and applying it to your content. If you don’t need the extra precision, continue using the set of touch objects that UIKit passes to the methods of your views or gesture recognizers.

 Coalesced touches are intended for apps that need the extra precision and can handle the associated costs. Processing coalesced touches means gathering additional data and applying it to your content. If you don’t need the extra precision, continue using the set of touch objects that UIKit passes to the methods of your views or gesture recognizers.

The following image illustrates what happens when the user drags Apple Pencil across the device. At the point where UIKit reports a touch event to the app, Apple Pencil has reported four touch positions, but UIKit reports only the last touch to the app by default. The remaining three touches are delivered as coalesced touches, and the app must retrieve them explicitly to use them.

![An illustration, with two iPad screens shown side by side. On the left, the initial touch event made by Apple Pencil is shown toward the upper-left of the display. As Apple Pencil is dragged down and to the right, the touches are coalesced when the drag ends, as shown on the right.](https://docs-assets.developer.apple.com/published/223d4aea70e73c49f05b65c59c288f41/media-3004383%402x.png)

To retrieve coalesced touches, call the [`coalescedTouches(for:)`](uievent/coalescedtouches(for:).md) method of the [`UIEvent`](uievent.md) object containing the original [`UITouch`](uitouch.md) object. That method returns the array of all touches since the last event, including the last [`UITouch`](uitouch.md) object actually delivered to the app. You must retrieve coalesced touches immediately when handling an event. After handling the event, there’s no guarantee that any coalesced touches will remain available.

## Topics

### Example
- [Implementing coalesced touch support in an app](implementing-coalesced-touch-support-in-an-app.md)
  Learn how to create a simple app that handles coalesced touches.

## See Also

- [Implementing a Multi-Touch app](implementing-a-multi-touch-app.md)
  Learn how to create a simple app that handles multitouch input.
- [Minimizing latency with predicted touches](minimizing-latency-with-predicted-touches.md)
  Create a smooth and responsive drawing experience using UIKit’s predictions for touch locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/getting-high-fidelity-input-with-coalesced-touches)*