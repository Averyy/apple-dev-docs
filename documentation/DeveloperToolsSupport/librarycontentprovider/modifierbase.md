# ModifierBase

**Framework**: DeveloperToolsSupport  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

A type to use as a base for modifier completions.

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
associatedtype ModifierBase = Any
```

#### Discussion

To verify that the completion for a modifier compiles, you specify modifiers as they apply to some base type. Since most modifiers can modify any SwiftUI view, you typically specify any concrete implementation of the [`View`](../../SwiftUI/view.md) protocol for `ModifierBase`. However, some modifiers apply to more specific types, like [`Image`](../../SwiftUI/image.md) or [`Text`](../../SwiftUI/text.md), or to an entirely different type like [`Shape`](../../SwiftUI/shape.md).

## See Also

### Adding Modifiers
- [func modifiers(base: Self.ModifierBase) -> [LibraryItem]](./modifiers%28base%29.md)
  Indicates a collection of SwiftUI view modifiers to add to the Xcode library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/librarycontentprovider/modifierbase)*