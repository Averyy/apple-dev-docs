# previewLayout(_:)

**Framework**: FamilyControls  
**Kind**: method

Overrides the size of the container for the preview.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func previewLayout(_ value: PreviewLayout) -> some View
```

#### Return Value

A preview that uses the given layout.

#### Discussion

By default, previews use the `PreviewLayout/device` layout, which places the view inside a visual representation of the chosen device. You can instead tell a preview to use a different layout by choosing one of the `PreviewLayout` values, like `PreviewLayout/sizeThatFits`:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewLayout(.sizeThatFits)
    }
}
```

## Parameters

- `value`: A layout to use for preview.

## See Also

- [func previewDevice(PreviewDevice?) -> some View](familyactivitypicker/previewdevice(_:).md)
  Overrides the device for a preview.
- [func previewDisplayName(String?) -> some View](familyactivitypicker/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](familyactivitypicker/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.
- [func previewContext<C>(C) -> some View](familyactivitypicker/previewcontext(_:).md)
  Declares a context for the preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/previewlayout(_:))*