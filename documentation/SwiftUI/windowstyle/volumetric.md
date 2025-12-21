# volumetric

**Framework**: SwiftUI  
**Kind**: property

A window style that creates a 3D volumetric window.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static var volumetric: VolumetricWindowStyle { get }
```

#### Discussion

Use a volumetric window — or a  — to display 3D content within a bounded region. For example, [`Hello World`](https://developer.apple.com/documentation/visionOS/World) uses a volume to present a `Globe` model that people can pick up and move around the Shared Space using the window bar:

```swift
WindowGroup(id: Module.globe.name) {
    Globe()
        .environment(model)
}
.windowStyle(.volumetric)
.defaultSize(width: 0.6, height: 0.6, depth: 0.6, in: .meters)
```

A volume enables someone to view content from all angles, unlike other windows which fade out as people move around the window. Also unlike other windows, a volume uses fixed scale, which means that objects in the volume appear smaller when the volume is farther away, like real objects would. For a comparison of fixed and dynamic scale, see [`Spatial layout`](https://developer.apple.com/design/Human-Interface-Guidelines/spatial-layout#Scale) in the Human Interface Guidelines.

You can specify a size for the volume using one of the default size scene modifiers, like [`defaultSize(width:height:depth:in:)`](scene/defaultsize(width:height:depth:in:).md). Because volumes use fixed scale, it’s typically convenient to specify a size in physical units — like meters, as the above code demonstrates. People can’t change the size of the volume after it appears.

> **Note**: Use this style only with [`WindowGroup`](windowgroup.md). Windows that you create using [`Window`](window.md) don’t support the volumetric window style.

For design guidance, see [`Windows`](https://developer.apple.com/design/Human-Interface-Guidelines/windows#Volumes) in the Human Interface Guidelines. If you want to place 3D objects arbitrarily throughout the Shared Space or in a Full Space, use an [`ImmersiveSpace`](immersivespace.md) instead.

## See Also

- [static var automatic: DefaultWindowStyle](windowstyle/automatic.md)
  The default window style.
- [static var hiddenTitleBar: HiddenTitleBarWindowStyle](windowstyle/hiddentitlebar.md)
  A window style which hides both the window’s title and the backing of the titlebar area, allowing more of the window’s content to show.
- [static var plain: PlainWindowStyle](windowstyle/plain.md)
  The plain window style.
- [static var titleBar: TitleBarWindowStyle](windowstyle/titlebar.md)
  A window style which displays the title bar section of the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowstyle/volumetric)*