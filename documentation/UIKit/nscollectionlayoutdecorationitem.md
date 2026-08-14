# NSCollectionLayoutDecorationItem

**Framework**: UIKit  
**Kind**: class

An object used to add a background to a section of a collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class NSCollectionLayoutDecorationItem
```

#### Overview

Each type of decoration item must have a unique element kind. Consider tracking these strings together in a way that makes it straightforward to identify each element, for example:

**Swift**:

```swift
struct ElementKind {
    static let badge = "badge-element-kind"
    static let background = "background-element-kind"
    static let sectionHeader = "section-header-element-kind"
    static let sectionFooter = "section-footer-element-kind"
    static let layoutHeader = "layout-header-element-kind"
    static let layoutFooter = "layout-footer-element-kind"
}
```

**Objective-C**:

```objc
NSString* const ELEMENT_KIND_BADGE = @"badge-element-kind";
NSString* const ELEMENT_KIND_BACKGROUND = @"background-element-kind";
NSString* const ELEMENT_KIND_SECTION_HEADER = @"section-header-element-kind";
NSString* const ELEMENT_KIND_SECTION_FOOTER = @"section-footer-element-kind";
NSString* const ELEMENT_KIND_LAYOUT_HEADER = @"layout-header-element-kind";
NSString* const ELEMENT_KIND_LAYOUT_FOOTER = @"layout-footer-element-kind";
```

Add a background to a section by setting that section’s [`decorationItems`](nscollectionlayoutsection/decorationitems.md) property:

**Swift**:

```swift
let sectionBackground = NSCollectionLayoutDecorationItem.background(
        elementKind: ElementKind.background)

section.decorationItems = [sectionBackground]

let layout = UICollectionViewCompositionalLayout(section: section)
layout.register(
    SectionBackgroundDecorationView.self,
    forDecorationViewOfKind: ElementKind.background)
return layout
```

**Objective-C**:

```objc
NSCollectionLayoutDecorationItem *sectionBackground = [NSCollectionLayoutDecorationItem backgroundDecorationItemWithElementKind: ELEMENT_KIND_BACKGROUND];

[section setDecorationItems: @[sectionBackground]];

UICollectionViewCompositionalLayout *layout = [[UICollectionViewCompositionalLayout alloc] initWithSection: section];
[layout registerClass: [SectionBackgroundDecorationView class] forDecorationViewOfKind: ELEMENT_KIND_BACKGROUND];
return layout;
```

## Topics

### Creating a background
- [class func background(elementKind: String) -> Self](nscollectionlayoutdecorationitem/background(elementkind:).md)
  Creates a section background with a string to identify the element kind.
### Getting the element kind
- [var elementKind: String](nscollectionlayoutdecorationitem/elementkind.md)
  A string that identifies the type of decoration item.
### Specifying stacking order
- [var zIndex: Int](nscollectionlayoutdecorationitem/zindex.md)
  The vertical stacking order of the decoration item in relation to other items in the section.

## Relationships

### Inherits From
- [NSCollectionLayoutItem](nscollectionlayoutitem.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class NSCollectionLayoutAnchor](nscollectionlayoutanchor.md)
  An object that defines how to attach a supplementary item to an item in a collection view.
- [class NSCollectionLayoutSupplementaryItem](nscollectionlayoutsupplementaryitem.md)
  An object used to add an extra visual decoration to an item in a collection view.
- [class NSCollectionLayoutBoundarySupplementaryItem](nscollectionlayoutboundarysupplementaryitem.md)
  An object used to add headers or footers to a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutdecorationitem)*