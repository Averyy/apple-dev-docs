# ModifierBase

**Framework**: DeveloperToolsSupport  
**Kind**: associatedtype  
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

To verify that the completion for a modifier compiles, you specify modifiers as they apply to some base type. Since most modifiers can modify any SwiftUI view, you typically specify any concrete implementation of the [`View`](https://developer.apple.com/documentation/SwiftUI/View) protocol for `ModifierBase`. However, some modifiers apply to more specific types, like [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) or [`Text`](https://developer.apple.com/documentation/SwiftUI/Text), or to an entirely different type like [`Shape`](https://developer.apple.com/documentation/SwiftUI/Shape).

## See Also

- [func modifiers(base: Self.ModifierBase) -> [LibraryItem]](librarycontentprovider/modifiers(base:).md)
  Indicates a collection of SwiftUI view modifiers to add to the Xcode library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/librarycontentprovider/modifierbase)*