# systemRouteController:handleEvent:completionHandler:

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method

Connects to, or disconnects from, a device when a user requests it in the picker.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (void) systemRouteController:(AVSystemRouteController *) controller handleEvent:(AVSystemRouteEvent *) event completionHandler:(void (^)(BOOL success)) completionHandler;
```

## Parameters

- `controller`: The system routing controller.
- `event`: The routing event to handle.
- `completionHandler`: A completion handler to call after processing the event. Pass `YES` if the event was handled successfully, `NO` otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontrollerobserver-7p7a5/systemroutecontroller:handleevent:completionhandler:)*