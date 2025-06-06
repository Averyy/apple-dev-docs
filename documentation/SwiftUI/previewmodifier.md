# PreviewModifier

**Framework**: SwiftUI  
**Kind**: protocol

A type that defines an environment in which previews can appear.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
protocol PreviewModifier
```

#### Overview

Conforming types can define shared contexts that will be cached by the preview system, then reused across participating previews. For example, you might create a model container here and populate it with sample data; in your `body` method you would then apply it to the preview using the `.modelContainer` view modifier.

```swift
struct SampleData: PreviewModifier {
    static func makeSharedContext() throws -> ModelContainer {
        let container = try ModelContainer(for: Snack.self)
        container.mainContext.insert(Snack.potatoChips)
        return container
    }

    func body(content: Content, context: ModelContainer) -> some View {
        content.modelContainer(context)
    }
 }
```

Use the `.modifier` preview trait to attach modifiers to a preview.

```swift
#Preview(traits: .modifier(SampleData())) {
    @Previewable @Query var snacks: [Snack]
    return SnackView(snack: snacks.first!)
}
```

## Topics

### Associated Types
- [associatedtype Body : View](previewmodifier/body.md)
- [associatedtype Context = Void](previewmodifier/context.md)
### Instance Methods
- [func body(content: Self.Content, context: Self.Context) -> Self.Body](previewmodifier/body(content:context:).md)
  Modify a preview by applying the shared context.
### Type Aliases
- [PreviewModifier.Content](previewmodifier/content.md)
  The type-erased content of a preview.
### Type Methods
- [static func makeSharedContext() async throws -> Self.Context](previewmodifier/makesharedcontext.md)
  Create shared context to apply to previews. The context returned here will be cached and passed into the `body` method for every preview that applies a modifier of this type.

## See Also

- [macro Previewable()](previewable().md)
  Tag allowing a dynamic property to appear inline in a preview.
- [protocol PreviewProvider](previewprovider.md)
  A type that produces view previews in Xcode.
- [enum PreviewPlatform](previewplatform.md)
  Platforms that can run the preview.
- [func previewDisplayName(String?) -> some View](view/previewdisplayname(_:).md)
  Sets a user visible name to show in the canvas for a preview.
- [struct PreviewModifierContent](previewmodifiercontent.md)
  The type-erased content of a preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewmodifier)*