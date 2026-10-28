# prepare()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Prepares the generator to trigger feedback.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func prepare()
```

```objc
- (void) prepare;
```

## Discussion

When you call this method, the generator is placed into a prepared state for a short period of time. While the generator is prepared, you can trigger feedback with lower latency.

Think about when you can best prepare your generators. Call [`prepare()`](./prepare%28%29.md) before the event that triggers feedback. The system needs time to prepare the Taptic Engine for minimal latency. Calling [`prepare()`](./prepare%28%29.md) and then immediately triggering feedback (without any time in between) does not improve latency.

To conserve power, the Taptic Engine returns to an idle state after any of the following events:

- You trigger feedback on the generator.
- A short period of time passes (typically seconds).
- The generator is deallocated.

After feedback is triggered, the Taptic Engine returns to its idle state. If you might trigger additional feedback within the next few seconds, immediately call [`prepare()`](./prepare%28%29.md) to keep the Taptic Engine in the prepared state.

You can also extend the prepared state by repeatedly calling the [`prepare()`](./prepare%28%29.md) method. However, if you continue calling [`prepare()`](./prepare%28%29.md) without ever triggering feedback, the system may eventually place the Taptic Engine back in an idle state and ignore any further [`prepare()`](./prepare%28%29.md) calls until after you trigger feedback at least once.

If you no longer need a prepared generator, remove all references to the generator object and let the system deallocate it. This lets the Taptic Engine return to its idle state.

> **Note**:  The [`prepare()`](./prepare%28%29.md) method is optional; however, it is highly recommended. Calling this method helps ensure that your feedback has the lowest possible latency.

## See Also

### Related Documentation
- [func selectionChanged()](../uiselectionfeedbackgenerator/selectionchanged%28%29.md)
  Triggers selection feedback.
- [func impactOccurred()](../uiimpactfeedbackgenerator/impactoccurred%28%29.md)
  Triggers impact feedback.
- [func notificationOccurred(UINotificationFeedbackGenerator.FeedbackType)](../uinotificationfeedbackgenerator/notificationoccurred%28_%29.md)
  Triggers notification feedback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifeedbackgenerator/prepare())*