# init(alignment:horizontalSpacing:verticalSpacing:)

**Framework**: SwiftUI  
**Kind**: init

Creates a grid with the specified spacing and alignment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(alignment: Alignment = .center, horizontalSpacing: CGFloat? = nil, verticalSpacing: CGFloat? = nil)
```

## Parameters

- `alignment`: The guide for aligning subviews within the   space allocated for a given cell. The default is   .
- `horizontalSpacing`: The horizontal distance between each cell, given   in points. The value is   by default, which results in a   default distance between cells that’s appropriate for the platform.
- `verticalSpacing`: The vertical distance between each cell, given   in points. The value is   by default, which results in a   default distance between cells that’s appropriate for the platform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gridlayout/init(alignment:horizontalspacing:verticalspacing:))*