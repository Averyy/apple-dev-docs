# help(_:)

**Framework**: FamilyControls  
**Kind**: method

Adds help text to a view using a string that you provide.

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
func help<S>(_ text: S) -> some View where S : StringProtocol
```

#### Discussion

Adding help to a view configures the view’s accessibility hint and its help tag (also called a ) in macOS or visionOS. For more information on using help tags, see [`Offering help`](https://developer.apple.com/design/Human-Interface-Guidelines/offering-help) in the Human Interface Guidelines.

```swift
Image(systemName: "pin.circle")
    .foregroundColor(pointOfInterest.tintColor)
    .help(pointOfInterest.name)
```

## Parameters

- `text`: The text to use as help.

## See Also

- [func help(Text) -> some View](familyactivitypicker/help(_:)-5nten.md)
  Adds help text to a view using a text view that you provide.
- [func help(LocalizedStringKey) -> some View](familyactivitypicker/help(_:)-pa0w.md)
  Adds help text to a view using a localized string that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/help(_:)-30gcc)*