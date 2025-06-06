# help(_:)

**Framework**: FamilyControls  
**Kind**: method

Adds help text to a view using a text view that you provide.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
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

```swift
Slider("Opacity", value: $selectedShape.opacity)
    .help(Text("Adjust the opacity of the selected \(selectedShape.name)"))
```

## Parameters

- `text`: The   view to use as help.

## See Also

- [func help<S>(S) -> some View](familyactivitypicker/help(_:)-30gcc.md)
  Adds help text to a view using a string that you provide.
- [func help(LocalizedStringKey) -> some View](familyactivitypicker/help(_:)-pa0w.md)
  Adds help text to a view using a localized string that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/help(_:)-5nten)*