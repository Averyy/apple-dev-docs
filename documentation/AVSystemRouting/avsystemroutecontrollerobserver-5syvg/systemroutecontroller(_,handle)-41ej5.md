# systemRouteController(_:handle:)

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method

Connects to, or disconnects from, a device when a user requests it in the picker.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func systemRouteController(_ controller: AVSystemRouteController, handle event: AVSystemRouteEvent) async -> Bool
```

## Return Value

`true` if the event was handled successfully, `false` otherwise.

## Parameters

- `controller`: The system routing controller.
- `event`: The routing event to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontrollerobserver-5syvg/systemroutecontroller(_:handle:)-41ej5)*