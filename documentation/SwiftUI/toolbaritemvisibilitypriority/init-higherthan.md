# init(higherThan:)

**Framework**: SwiftUI  
**Kind**: init

Creates a priority higher than the specified value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
init(higherThan other: ToolbarItemVisibilityPriority)
```

#### Discussion

The priority is higher than `other` but doesn’t cross above the next higher system priority. For example, `ToolbarItemVisibilityPriority(higherThan: .high)` returns a value that is greater than `.high`.

Priorities created with the same base value are equal:

```swift
let x = ToolbarItemVisibilityPriority(higherThan: .high)
let y = ToolbarItemVisibilityPriority(higherThan: .high)
x == y // true
```

## See Also

- [init(lowerThan: ToolbarItemVisibilityPriority)](toolbaritemvisibilitypriority/init(lowerthan:).md)
  Creates a priority lower than the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority/init(higherthan:))*