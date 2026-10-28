# sticky(horizontal:vertical:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

## Return Value

A modified version of self sticking to dimensions specified

## Discussion

If `sticky` is `.vertical`, the presentation can grow in the vertical and horizontal dimensions when its content size grows, but will not shrink in the vertical dimension when content size shrinks.

```swift
ContentView()
  .sheet(isPresented: $presentSheet) {
    MyDynamicSheetContent()
      .presentationSizing(
        .form.sticky(horizontal: false, vertical: true))
  }
```

> **See Also**: [`fitted(horizontal:vertical:)`](./fitted%28horizontal,vertical%29.md)

## Parameters

- `horizontal`: A boolean indicating whether to maintain the largest size horizontally
- `vertical`: A boolean indicating whether to maintain the largest size vertically

## See Also

### Creating custom presentation size
- [func fitted(horizontal: Bool, vertical: Bool) -> some PresentationSizing](./fitted%28horizontal,vertical%29.md)
- [func proposedSize(for: PresentationSizingRoot, context: PresentationSizingContext) -> ProposedViewSize](./proposedsize%28for,context%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationsizing/sticky(horizontal:vertical:))*