# init(fieldOfView:requestDeviceFitUpdates:presentCoachingAlerts:)

**Framework**: ARKit  
**Kind**: init

Create a visual fidelity data provider.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(fieldOfView: VisualFidelityProvider.FieldOfView? = nil, requestDeviceFitUpdates: Bool = false, presentCoachingAlerts: Bool = false)
```

## Parameters

- `fieldOfView`: Field of view specification to monitor. Use Apple-defined presets (e.g., `.presetA`) or `.polygon(points:)` for precise geometric control. Pass `nil` to skip field of view monitoring. Default is `nil`.
- `requestDeviceFitUpdates`: When true, device fit status will be included in fidelity data updates. Default is false.
- `presentCoachingAlerts`: When true, system will automatically present user notifications with coaching tips when validation errors are detected. Default is false.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/visualfidelityprovider/init(fieldofview:requestdevicefitupdates:presentcoachingalerts:))*