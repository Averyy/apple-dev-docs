# previewInterfaceOrientation(_:)

**Framework**: FamilyControls  
**Kind**: method

Overrides the orientation of the preview.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func previewInterfaceOrientation(_ value: InterfaceOrientation) -> some View
```

#### Return Value

A preview that uses the given orientation.

#### Discussion

By default, device previews appear right side up, using orientation `InterfaceOrientation/portrait`. You can change the orientation of a preview using one of the values in the `InterfaceOrientation` structure:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewInterfaceOrientation(.landscapeRight)
    }
}
```

## Parameters

- `value`: An orientation to use for preview.

## See Also

- [func previewDevice(PreviewDevice?) -> some View](familyactivitypicker/previewdevice(_:).md)
  Overrides the device for a preview.
- [func previewDisplayName(String?) -> some View](familyactivitypicker/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [func previewLayout(PreviewLayout) -> some View](familyactivitypicker/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func previewContext<C>(C) -> some View](familyactivitypicker/previewcontext(_:).md)
  Declares a context for the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/previewinterfaceorientation(_:))*