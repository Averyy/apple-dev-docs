# subtitleColor

**Framework**: SwiftUI  
**Kind**: property

The color to apply to the subtitle text displayed in the short look interface. If `nil` the text will be the default system color.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency class var subtitleColor: Color? { get }
```

#### Discussion

Default value is `nil`

## See Also

- [class var coalescedDescriptionFormat: String?](wkusernotificationhostingcontroller/coalesceddescriptionformat.md)
  The format string to display when multiple notifications of the same type arrive simultaneously. If you specify a custom string, you can use the %d variable to reflect the number of notifications. If `nil` format will be the system default.
- [class var isInteractive: Bool](wkusernotificationhostingcontroller/isinteractive.md)
  If the notification should accept user input.
- [class var sashColor: Color?](wkusernotificationhostingcontroller/sashcolor.md)
  Color to use within the sash of the long look interface. If `nil` the sash will be the default system color.
- [class var titleColor: Color?](wkusernotificationhostingcontroller/titlecolor.md)
  The color to apply to the text displayed in the sash. If `nil` the text will be the default system color.
- [class var wantsSashBlur: Bool](wkusernotificationhostingcontroller/wantssashblur.md)
  If the sash should include a blur over the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkusernotificationhostingcontroller/subtitlecolor)*