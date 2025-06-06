# Previewable()

**Framework**: SwiftUI  
**Kind**: macro

Tag allowing a dynamic property to appear inline in a preview.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@attached
(peer) macro Previewable()
```

#### Overview

Tagging a variable declaration at root scope in your `#Preview` body with ‘@Previewable’ allows you to use dynamic properties inline in previews. The `#Preview` macro will generate an embedded SwiftUI view; tagged declarations become properties on the view, and all remaining statements form the view’s body.

```swift
#Preview("toggle") {
    @Previewable @State var toggled = true
    return Toggle("Loud Noises", isOn: $toggled)
}
```

It is an error to use `@Previewable` outside of a `#Preview` body closure.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewable())*