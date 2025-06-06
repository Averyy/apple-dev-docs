# previews

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

A collection of views to preview.

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
@ViewBuilder
@MainActor @preconcurrency static var previews: Self.Previews { get }
```

#### Discussion

Implement a computed `previews` property to indicate the content to preview. Xcode generates a preview for each view that you list. You can apply [`View`](view.md) modifiers to the views, like you do when creating a custom view. For a preview, you can also use various preview-specific modifiers that customize the preview. For example, you can choose a specific device for the preview by adding the [`previewDevice(_:)`](view/previewdevice(_:).md) modifier:

```swift
struct CircleImage_Previews: PreviewProvider {
    static var previews: some View {
        CircleImage()
            .previewDevice(PreviewDevice(rawValue: "iPad Pro (11-inch)"))
    }
}
```

For the full list of preview-specific modifiers, see [`Previews in Xcode`](previews-in-xcode.md).

## See Also

- [associatedtype Previews : View](previewprovider/previews-swift.associatedtype.md)
  The type to preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewprovider/previews-swift.type.property)*