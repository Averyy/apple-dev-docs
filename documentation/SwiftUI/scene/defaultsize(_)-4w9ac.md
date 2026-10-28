# defaultSize(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets a default size for a volumetric window.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
nonisolated
func defaultSize(_ size: Size3D) -> some Scene
```

**Other overloads**:

```swift
nonisolated
func defaultSize(_ size: CGSize) -> some Scene
```

## Return Value

A scene that uses a default size for new windows.

## Discussion

Use this modifier to indicate the default initial size for a new 3D window created from a [`Scene`](../scene.md) using [`VolumetricWindowStyle`](../volumetricwindowstyle.md):

```swift
WindowGroup {
    ContentView()
}
.windowStyle(.volumetric)
.defaultSize(Size3D(width: 600, height: 400, depth: 600))
```

Each parameter is specified in points. The size of a volumetric scene is immutable after creation.

This modifier affects only windows that have the volumetric style in visionOS.

## Parameters

- `size`: The default 3D size for the created window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scene/defaultsize(_:)-4w9ac)*