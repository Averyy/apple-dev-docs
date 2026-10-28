# listItemTint(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the tint effect for content in a list.

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
nonisolated
func listItemTint(_ tint: ListItemTint?) -> some View
```

**Other overloads**:

```swift
nonisolated
func listItemTint(_ tint: Color?) -> some View
```

## Discussion

The containing list’s style applies the tint as appropriate. For example, watchOS uses the tint color for its background platter appearance. Sidebars on iOS and macOS apply the tint color to their [`Label`](../label.md) icons, which otherwise use the accent color by default.

## Parameters

- `tint`: The tint effect to use. Use `nil` to avoid overriding the inherited tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/listitemtint(_:)-12mbh)*