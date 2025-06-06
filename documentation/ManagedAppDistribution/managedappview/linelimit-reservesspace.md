# lineLimit(_:reservesSpace:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Sets a limit for the number of lines text can occupy in this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func lineLimit(_ limit: Int, reservesSpace: Bool) -> some View
```

#### Discussion

Use this modifier to specify a limit to the lines that a `Text` or a vertical `TextField` may occupy. If passed a value of true for the `reservesSpace` parameter, and the text of such views occupies less space than the provided limit, that view expands to occupy the minimum number of lines. When the text occupies more space than the provided limit, a `Text` view truncates its content while a `TextField` becomes scrollable.

```None
GroupBox {
    Text("Title")
        .font(.headline)
        .lineLimit(2, reservesSpace: true)
    Text("Subtitle")
        .font(.subheadline)
        .lineLimit(4, reservesSpace: true)
}
```

## Parameters

- `limit`: The line limit.
- `reservesSpace`: Whether text reserves space so that   it always occupies the height required to display the specified   number of lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/linelimit(_:reservesspace:))*