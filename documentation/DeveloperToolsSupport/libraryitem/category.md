# LibraryItem.Category

**Framework**: DeveloperToolsSupport  
**Kind**: struct

The kinds of library items that you can create.

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
struct Category
```

#### Overview

When you specify a category for a library item, Xcode can group it with similar items in the library, making it easier for you to find. Categories provide visual treatment in the Xcode Library, but the treatment for each category depends on where the asset resides within the library.

## Topics

### Specifying a Category
- [static let control: LibraryItem.Category](libraryitem/category/control.md)
  A category for controls, like buttons and context menus.
- [static let effect: LibraryItem.Category](libraryitem/category/effect.md)
  A category for effects, like opacity and saturation modifiers.
- [static let layout: LibraryItem.Category](libraryitem/category/layout.md)
  A category for items that manage layout, like stack views and frame modifiers.
- [static let other: LibraryItem.Category](libraryitem/category/other.md)
  A general category.

## See Also

- [init<SnippetExpressionType>(@autoclosure () -> SnippetExpressionType, visible: Bool, title: String?, category: LibraryItem.Category, matchingSignature: String?)](libraryitem/init(_:visible:title:category:matchingsignature:).md)
  Creates a new library item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/libraryitem/category)*