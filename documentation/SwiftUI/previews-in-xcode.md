# Previews in Xcode

**Framework**: SwiftUI

Generate dynamic, interactive previews of your custom views.

#### Overview

When you create a custom [`View`](view.md) with SwiftUI, Xcode can display a preview of the view’s content that stays up-to-date as you make changes to the view’s code. You use one of the preview macros — like [`Preview(_:body:)`](preview(_:body:).md) — to tell Xcode what to display. Xcode shows the preview in a canvas beside your code.

![None](https://docs-assets.developer.apple.com/published/5efb20dd844dbf1610ee3a4c833f809b/previews-in-xcode-hero%402x.png)

Different preview macros enable different kinds of configuration. For example, you can add traits that affect the preview’s appearance using the [`Preview(_:traits:_:body:)`](preview(_:traits:_:body:).md) macro or add custom viewpoints for the preview using the [`Preview(_:traits:body:cameras:)`](preview(_:traits:body:cameras:).md) macro. You can also check how your view behaves inside a specific scene type. For example, in visionOS you can use the [`Preview(_:immersionStyle:traits:body:)`](preview(_:immersionstyle:traits:body:).md) macro to preview your view inside an [`ImmersiveSpace`](immersivespace.md).

You typically rely on preview macros to create previews in your code. However, if you can’t get the behavior you need using a preview macro, you can use the [`PreviewProvider`](previewprovider.md) protocol and its associated supporting types to define and configure a preview.

## Topics

### Essentials
- [Previewing your app’s interface in Xcode](../Xcode/previewing-your-apps-interface-in-xcode.md)
  Iterate designs quickly and preview your apps’ displays across different Apple devices.
### Creating a preview
- [macro Preview(String?, body: () -> any View)](preview(_:body:).md)
  Creates a preview of a SwiftUI view.
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>, PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](preview(_:traits:_:body:).md)
  Creates a preview of a SwiftUI view using the specified traits.
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](preview(_:traits:body:cameras:).md)
  Creates a preview of a SwiftUI view using the specified traits and custom viewpoints.
### Creating a preview in the context of a scene
- [macro Preview<Style>(String?, immersionStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](preview(_:immersionstyle:traits:body:).md)
  Creates a preview of a SwiftUI view in an immersive space.
- [macro Preview<Style>(String?, immersionStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](preview(_:immersionstyle:traits:body:cameras:).md)
  Creates a preview of a SwiftUI view in an immersive space with custom viewpoints.
- [macro Preview<Style>(String?, windowStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View)](preview(_:windowstyle:traits:body:).md)
  Creates a preview of a SwiftUI view in a window.
- [macro Preview<Style>(String?, windowStyle: Style, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> any View, cameras: () -> [PreviewCamera])](preview(_:windowstyle:traits:body:cameras:).md)
  Creates a preview of a SwiftUI view in a window with custom viewpoints.
### Defining a preview
- [macro Previewable()](previewable().md)
  Tag allowing a dynamic property to appear inline in a preview.
- [protocol PreviewProvider](previewprovider.md)
  A type that produces view previews in Xcode.
- [enum PreviewPlatform](previewplatform.md)
  Platforms that can run the preview.
- [func previewDisplayName(String?) -> some View](view/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [protocol PreviewModifier](previewmodifier.md)
  A type that defines an environment in which previews can appear.
- [struct PreviewModifierContent](previewmodifiercontent.md)
  The type-erased content of a preview.
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
### Building in debug mode
- [struct DebugReplaceableView](debugreplaceableview.md)
  Erases view opaque result types in debug builds.

## See Also

- [Xcode library customization](xcode-library-customization.md)
  Expose custom views and modifiers in the Xcode library.
- [Performance analysis](performance-analysis.md)
  Measure and improve your app’s responsiveness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previews-in-xcode)*