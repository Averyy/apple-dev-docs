# onMapCameraChange(frequency:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Performs an action when Map camera framing changes

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency func onMapCameraChange(frequency: MapCameraUpdateFrequency = .onEnd, _ action: @escaping (MapCameraUpdateContext) -> Void) -> some View
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func onMapCameraChange(frequency: MapCameraUpdateFrequency = .onEnd, _ action: @escaping () -> Void) -> some View
```

## Parameters

- `frequency`: How frequently the action should be performed during a camera interaction.
- `action`: A closure to run when the camera framing changes. The closure takes a `MapCameraUpdateContext` parameter that indicates the camera and the framed area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onmapcamerachange(frequency:_:)-2pcga)*