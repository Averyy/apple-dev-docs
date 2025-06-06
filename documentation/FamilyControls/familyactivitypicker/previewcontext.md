# previewContext(_:)

**Framework**: FamilyControls  
**Kind**: method

Declares a context for the preview.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func previewContext<C>(_ value: C) -> some View where C : PreviewContext
```

## Parameters

- `value`: The context for the preview; the default is  .

## See Also

- [func previewDevice(PreviewDevice?) -> some View](familyactivitypicker/previewdevice(_:).md)
  Overrides the device for a preview.
- [func previewDisplayName(String?) -> some View](familyactivitypicker/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [func previewLayout(PreviewLayout) -> some View](familyactivitypicker/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](familyactivitypicker/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/previewcontext(_:))*