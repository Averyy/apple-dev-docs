# help(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Adds help text to a view using a text view that you provide.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func help(_ text: Text) -> some View
```

#### Discussion

Adding help to a view configures the view’s accessibility hint and its help tag (also called a ) in macOS or visionOS. For more information on using help tags, see [`Offering help`](https://developer.apple.com/design/Human-Interface-Guidelines/offering-help) in the Human Interface Guidelines.

```None
Slider("Opacity", value: $selectedShape.opacity)
    .help(Text("Adjust the opacity of the selected \(selectedShape.name)"))
```

## Parameters

- `text`: The   view to use as help.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/help(_:)-6s0zs)*