# LibraryContentProvider

**Framework**: DeveloperToolsSupport  
**Kind**: protocol

A source of Xcode library and code completion content.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
protocol LibraryContentProvider
```

#### Overview

Xcode discovers implementations of the `LibraryContentProvider` protocol in your project or workspace and examines their contents for items that it can add to the Xcode library. Add views by implementing the content provider’s computed [`views`](librarycontentprovider/views.md) property, and returning an array of [`LibraryItem`](libraryitem.md) instances initialized with the views you want to publish:

```swift
struct LibraryViewContent: LibraryContentProvider {
    var views: [LibraryItem] {
        LibraryItem(MyView())
    }
}
```

Add view modifiers by implementing the [`modifiers(base:)`](librarycontentprovider/modifiers(base:).md) method and similarly returning an array of library items initialized with the modifiers you want to publish. For view modifiers, you also specify the type to which the modifiers apply:

```swift
struct LibraryModifierContent: LibraryContentProvider {
    func modifiers(base: MyView) -> [LibraryItem] {
        LibraryItem(base.myModifier(value: MyValue()))
    }
}
```

For modifiers that you define in an extension to [`View`](https://developer.apple.com/documentation/SwiftUI/View), you can provide any view conformer as the `base`. For modifiers that you define on a particular view type, provide that type as the `base`.

## Topics

### Adding Views
- [var views: [LibraryItem]](librarycontentprovider/views.md)
  The SwiftUI views that you want to add to the Xcode library.
### Adding Modifiers
- [func modifiers(base: Self.ModifierBase) -> [LibraryItem]](librarycontentprovider/modifiers(base:).md)
  Indicates a collection of SwiftUI view modifiers to add to the Xcode library.
- [associatedtype ModifierBase = Any](librarycontentprovider/modifierbase.md)
  A type to use as a base for modifier completions.
### Building Arrays
- [struct LibraryContentBuilder](librarycontentbuilder.md)
  A function builder for generating arrays of library items without requiring full array literal syntax.

## See Also

- [struct LibraryItem](libraryitem.md)
  A single item to add to the Xcode library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/librarycontentprovider)*