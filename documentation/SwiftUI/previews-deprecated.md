# Deprecated

**Framework**: SwiftUI

Review deprecated preview symbols and their replacements.

## Topics

### Defining a preview
- [protocol PreviewProvider](previewprovider.md)
  A type that produces view previews in Xcode.
- [enum PreviewPlatform](previewplatform.md)
  Platforms that can run the preview.
- [func previewDisplayName(String?) -> some View](view/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
### Customizing a preview
- [func previewDevice(PreviewDevice?) -> some View](view/previewdevice(_:).md)
  Overrides the device for a preview.
- [struct PreviewDevice](previewdevice.md)
  A simulator device that runs a preview.
- [func previewLayout(PreviewLayout) -> some View](view/previewlayout(_:).md)
  Overrides the size of the container for the preview.
- [func previewInterfaceOrientation(InterfaceOrientation) -> some View](view/previewinterfaceorientation(_:).md)
  Overrides the orientation of the preview.
- [struct InterfaceOrientation](interfaceorientation.md)
  The orientation of the interface from the user’s perspective.
### Setting a context
- [func previewContext<C>(C) -> some View](view/previewcontext(_:).md)
  Declares a context for the preview.
- [protocol PreviewContext](previewcontext.md)
  A context type for use with a preview.
- [protocol PreviewContextKey](previewcontextkey.md)
  A key type for a preview context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previews-deprecated)*