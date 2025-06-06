# previewDisplayName(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets a user visible name to show in the canvas for a preview.

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
nonisolated
func previewDisplayName(_ value: String?) -> some View
```

#### Return Value

A preview that uses the given name.

#### Discussion

Apply this modifier to a view inside your [`PreviewProvider`](previewprovider.md) implementation to associate a display name with that view’s preview:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewDisplayName("Circle")
    }
}
```

![A screenshot of the Xcode preview canvas cropped to just the top of a](https://docs-assets.developer.apple.com/published/af4f6594769133bd756945b236c1583e/View-previewDisplayName-1%402x.png)

Add a name when you have multiple previews together in the canvas that you need to tell apart. The default value is `nil`, in which case Xcode displays a default string.

## Parameters

- `value`: A name for the preview.

## See Also

- [macro Previewable()](previewable().md)
  Tag allowing a dynamic property to appear inline in a preview.
- [protocol PreviewProvider](previewprovider.md)
  A type that produces view previews in Xcode.
- [enum PreviewPlatform](previewplatform.md)
  Platforms that can run the preview.
- [protocol PreviewModifier](previewmodifier.md)
  A type that defines an environment in which previews can appear.
- [struct PreviewModifierContent](previewmodifiercontent.md)
  The type-erased content of a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/previewdisplayname(_:))*