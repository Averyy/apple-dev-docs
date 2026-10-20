# titleColor

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The color to apply to the text displayed in the sash. If `nil` the text will be the default system color.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
@MainActor
@preconcurrency class var titleColor: Color? { get }
```

#### Discussion

Default value is `nil`

## See Also

### Configuring the notification
- [class var coalescedDescriptionFormat: String?](./coalesceddescriptionformat.md)
  The format string to display when multiple notifications of the same type arrive simultaneously. If you specify a custom string, you can use the %d variable to reflect the number of notifications. If `nil` format will be the system default.
- [class var isInteractive: Bool](./isinteractive.md)
  If the notification should accept user input.
- [class var sashColor: Color?](./sashcolor.md)
  Color to use within the sash of the long look interface. If `nil` the sash will be the default system color.
- [class var subtitleColor: Color?](./subtitlecolor.md)
  The color to apply to the subtitle text displayed in the short look interface. If `nil` the text will be the default system color.
- [class var wantsSashBlur: Bool](./wantssashblur.md)
  If the sash should include a blur over the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/wkusernotificationhostingcontroller/titlecolor)*