# PreviewProvider

**Framework**: SwiftUI  
**Kind**: protocol

A type that produces view previews in Xcode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol PreviewProvider : _PreviewProvider
```

#### Overview

> ❗ **Important**: You can use this protocol to define a preview manually, but you typically use a preview macro like [`Preview(_:body:)`](preview(_:body:).md) instead.

You can create an Xcode preview by declaring a structure that conforms to the `PreviewProvider` protocol. Implement the required [`previews`](previewprovider/previews-swift.type.property.md) computed property, and return the view to display:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
    }
}
```

Xcode statically discovers preview providers in your project and generates previews for any providers currently open in the source editor. Xcode generates the preview using the current run destination as a hint for which device to display. For example, Xcode shows the following preview if you’ve selected an iOS target to run on the iPhone 12 Pro Max simulator:

![A screenshot of the Xcode canvas previewing a circular image on an](https://docs-assets.developer.apple.com/published/2bc550d5f4210c90f0d4b170a06eecf7/PreviewProvider-1%402x.png)

When you create a new file (File > New > File) and choose the SwiftUI view template, Xcode automatically inserts a preview structure at the bottom of the file that you can configure. You can also create new preview structures in an existing SwiftUI view file by choosing Editor > Create Preview.

Customize the preview’s appearance by adding view modifiers, just like you do when building a custom [`View`](view.md). This includes preview-specific modifiers that let you control aspects of the preview, like the device orientation:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewInterfaceOrientation(.landscapeLeft)
    }
}
```

![A screenshot of the Xcode canvas previewing a circular image on an](https://docs-assets.developer.apple.com/published/76fa7544938a92051e4704241e7aec57/PreviewProvider-2%402x.png)

For the complete list of preview customizations, see [`Previews in Xcode`](previews-in-xcode.md).

Xcode creates different previews for each view in your preview, so you can see variations side by side. For example, you might want to see a view’s light and dark appearances simultaneously:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
        CircleImage()
            .preferredColorScheme(.dark)
    }
}
```

Use a [`Group`](group.md) when you want to maintain different previews, but apply a single modifier to all of them:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            CircleImage()
            CircleImage()
                .preferredColorScheme(.dark)
        }
        .previewLayout(.sizeThatFits)
    }
}
```

![A screenshot of the Xcode canvas previewing a circular image twice,](https://docs-assets.developer.apple.com/published/2fafcc23213fe86c87888bfffb1d96a4/PreviewProvider-3%402x.png)

## Topics

### Creating a preview
- [static var previews: Self.Previews](previewprovider/previews-swift.type.property.md)
  A collection of views to preview.
- [associatedtype Previews : View](previewprovider/previews-swift.associatedtype.md)
  The type to preview.
### Specifying the platform
- [static var platform: PreviewPlatform?](previewprovider/platform.md)
  The platform on which to run the provider.

## See Also

- [macro Previewable()](previewable().md)
  Tag allowing a dynamic property to appear inline in a preview.
- [enum PreviewPlatform](previewplatform.md)
  Platforms that can run the preview.
- [func previewDisplayName(String?) -> some View](view/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [protocol PreviewModifier](previewmodifier.md)
  A type that defines an environment in which previews can appear.
- [struct PreviewModifierContent](previewmodifiercontent.md)
  The type-erased content of a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewprovider)*