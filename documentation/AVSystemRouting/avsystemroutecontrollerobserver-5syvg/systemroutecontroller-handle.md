# systemRouteController(_:handle:)

**Framework**: AVSystemRouting  
**Kind**: method  
**Required**: Yes

Connects to, or disconnects from, a device when a user requests it in the picker.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
func systemRouteController(_ controller: AVSystemRouteController, handle event: AVSystemRouteEvent) async -> Bool
```

## Parameters

- `controller`: The system routing controller.
- `event`: The routing event to handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutecontrollerobserver-5syvg/systemroutecontroller(_:handle:))*