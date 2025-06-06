# UIPress.PressType

**Framework**: UIKit  
**Kind**: enum

Constants that represent buttons that a person can press.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum PressType
```

## Topics

### Actions
- [UIPress.PressType.playPause](uipress/presstype/playpause.md)
  A constant that represents the play/pause button.
- [UIPress.PressType.select](uipress/presstype/select.md)
  A constant that represents the select button.
- [UIPress.PressType.menu](uipress/presstype/menu.md)
  A constant that represents the menu button.
### Navigation
- [UIPress.PressType.upArrow](uipress/presstype/uparrow.md)
  A constant that represents the up arrow button.
- [UIPress.PressType.downArrow](uipress/presstype/downarrow.md)
  A constant that represents the down arrow button.
- [UIPress.PressType.leftArrow](uipress/presstype/leftarrow.md)
  A constant that represents the left arrow button.
- [UIPress.PressType.rightArrow](uipress/presstype/rightarrow.md)
  A constant that represents the right arrow button.
- [UIPress.PressType.pageDown](uipress/presstype/pagedown.md)
  A constant that represents the page down button.
- [UIPress.PressType.pageUp](uipress/presstype/pageup.md)
  A constant that represents the page up button.
### Enumeration Cases
- [UIPress.PressType.tvRemoteFourColors](uipress/presstype/tvremotefourcolors.md)
  Represents a button on a TV remote labeled with four colors, analogous to the four separate color buttons found on some TV remotes. When this button is pressed, an app should perform the appropriate color action or if there are multiple color actions available provide UI to choose the specific color.
- [UIPress.PressType.tvRemoteOneTwoThree](uipress/presstype/tvremoteonetwothree.md)
  Represents a button on a TV remote labeled with 123. When this button is pressed, an app should provide UI to enter a specific channel number if channel numbers are available. If no channel numbers exist the app should provide UI to toggle channel category filters, search for channels by name or search for currently airing shows.
### Initializers
- [init?(rawValue: Int)](uipress/presstype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [UIPress.Phase](uipress/phase-swift.enum.md)
  Constants that represent the phases of a button press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/presstype)*