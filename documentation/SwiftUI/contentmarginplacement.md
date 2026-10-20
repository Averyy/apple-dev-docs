# ContentMarginPlacement

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

The placement of margins.

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
struct ContentMarginPlacement
```

#### Overview

Different views can support customizating margins that appear in different parts of that view. Use values of this type to customize those margins of a particular placement.

For example, use a [`scrollIndicators`](./contentmarginplacement/scrollindicators.md) placement to customize the margins of scrollable view’s scroll indicators separately from the margins of a scrollable view’s content.

Use this type with the [`contentMargins(_:for:)`](./view/contentmargins%28_,for%29.md) modifier.

## Topics

### Getting the placement
- [static var automatic: ContentMarginPlacement](./contentmarginplacement/automatic.md)
  The automatic placement.
- [static var scrollContent: ContentMarginPlacement](./contentmarginplacement/scrollcontent.md)
  The scroll content placement.
- [static var scrollIndicators: ContentMarginPlacement](./contentmarginplacement/scrollindicators.md)
  The scroll indicators placement.

## See Also

### Setting margins
- [func contentMargins(CGFloat, for: ContentMarginPlacement) -> some View](./view/contentmargins%28_,for%29.md)
  Configures the content margin for a provided placement.
- [func contentMargins(_:_:for:)](./view/contentmargins%28_,_,for%29.md)
  Configures the content margin for a provided placement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/contentmarginplacement)*