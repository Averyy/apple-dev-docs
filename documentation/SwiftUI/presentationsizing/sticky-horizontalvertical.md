# sticky(horizontal:vertical:)

**Framework**: Swiftui  
**Kind**: method

Modifies self to be sticky in the specified dimensions — growing, but not shrinking.

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
func sticky(horizontal: Bool = false, vertical: Bool = false) -> some PresentationSizing
```

#### Return Value

A modified version of self sticking to dimensions specified

#### Discussion

If `sticky` is `.vertical`, the presentation can grow in the vertical and horizontal dimensions when its content size grows, but will not shrink in the vertical dimension when content size shrinks.

```swift
ContentView()
  .sheet(isPresented: $presentSheet) {
    MyDynamicSheetContent()
      .presentationSizing(
        .form.sticky(horizontal: false, vertical: true))
  }
```

> **Note**: [`fitted(horizontal:vertical:)`](presentationsizing/fitted(horizontal:vertical:).md)

## Parameters

- `horizontal`: A boolean indicating whether to maintain the largest   size horizontally
- `vertical`: A boolean indicating whether to maintain the largest size   vertically

## See Also

- [func fitted(horizontal: Bool, vertical: Bool) -> some PresentationSizing](presentationsizing/fitted(horizontal:vertical:).md)
- [func proposedSize(for: PresentationSizingRoot, context: PresentationSizingContext) -> ProposedViewSize](presentationsizing/proposedsize(for:context:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationsizing/sticky(horizontal:vertical:))*