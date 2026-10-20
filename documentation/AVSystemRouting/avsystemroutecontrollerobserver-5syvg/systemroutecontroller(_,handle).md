# systemRouteController(_:handle:)

**Framework**: AVSystemRouting  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Connects to, or disconnects from, a device when a user requests it in the picker.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
func systemRouteController(_ controller: AVSystemRouteController, handle event: AVSystemRouteEvent) async -> Bool
```

## Parameters

- `controller`: The system routing controller.
- `event`: The routing event to handle.

## Default Implementations

### AVSystemRouteControllerObserver Implementations
- [func systemRouteController(AVSystemRouteController, handle: AVSystemRouteEvent) async -> Bool](./systemroutecontroller%28_,handle%29-41ej5.md)
  Connects to, or disconnects from, a device when a user requests it in the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontrollerobserver-5syvg/systemroutecontroller(_:handle:))*