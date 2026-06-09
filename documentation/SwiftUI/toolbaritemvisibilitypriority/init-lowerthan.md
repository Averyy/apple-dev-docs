# init(lowerThan:)

**Framework**: SwiftUI  
**Kind**: init

Creates a priority lower than the specified value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)

## Declaration

```swift
init(lowerThan other: ToolbarItemVisibilityPriority)
```

#### Discussion

The priority is lower than `other` but doesn’t cross below the next lower system priority. For example, `ToolbarItemVisibilityPriority(lowerThan: .high)` returns a value that is less than `.high` but greater than `.automatic`.

Priorities created with the same base value are equal:

```swift
let x = ToolbarItemVisibilityPriority(lowerThan: .high)
let y = ToolbarItemVisibilityPriority(lowerThan: .high)
x == y // true
```

## See Also

- [init(higherThan: ToolbarItemVisibilityPriority)](toolbaritemvisibilitypriority/init(higherthan:).md)
  Creates a priority higher than the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/toolbaritemvisibilitypriority/init(lowerthan:))*