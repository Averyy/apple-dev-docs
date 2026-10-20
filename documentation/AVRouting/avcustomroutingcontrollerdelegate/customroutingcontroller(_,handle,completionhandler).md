# customRoutingController(_:handle:completionHandler:)

**Framework**: AVRouting  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Connects to, or disconnects from, a device when a user requests it in the picker.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func customRoutingController(_ controller: AVCustomRoutingController, handle event: AVCustomRoutingEvent, completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
func customRoutingController(_ controller: AVCustomRoutingController, handle event: AVCustomRoutingEvent) async -> Bool
```

```objc
- (void) customRoutingController:(AVCustomRoutingController *) controller handleEvent:(AVCustomRoutingEvent *) event completionHandler:(void (^)(BOOL success)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func customRoutingController(_ controller: AVCustomRoutingController, handle event: AVCustomRoutingEvent) async -> Bool
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

## Parameters

- `controller`: A custom routing controller.
- `event`: The routing event to handle.
- `completionHandler`: A completion handler to call after processing the event. Pass [`true`](../../Swift/true.md) to the completion handler if the activation, reactivation, or deactivation of the route succeeds, and [`false`](../../Swift/false.md), otherwise.

## See Also

### Handling controller events
- [func customRoutingController(AVCustomRoutingController, eventDidTimeOut: AVCustomRoutingEvent)](./customroutingcontroller%28_,eventdidtimeout%29.md)
  Tells the delegate when a routing event times out.
- [func customRoutingController(AVCustomRoutingController, didSelect: AVCustomRoutingActionItem)](./customroutingcontroller%28_,didselect%29.md)
  Tells the delegate when a user selects a custom item in the route picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingcontrollerdelegate/customroutingcontroller(_:handle:completionhandler:))*