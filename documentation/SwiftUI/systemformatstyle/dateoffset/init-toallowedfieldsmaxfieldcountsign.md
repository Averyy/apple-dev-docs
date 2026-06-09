# init(to:allowedFields:maxFieldCount:sign:)

**Framework**: SwiftUI  
**Kind**: init

Creates a format style that displays the offset between a comparison date and an anchor date that you provide.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(to anchor: Date, allowedFields: Set<Date.ComponentsFormatStyle.Field> = [.year, .month, .week, .day, .hour, .minute, .second], maxFieldCount: Int = 2, sign: NumberFormatStyleConfiguration.SignDisplayStrategy = .automatic)
```

#### Discussion

The style uses a time-pattern representation (`3:46`) when `allowedFields` contains only `.minute` and `.second`, or contains `.hour`, `.minute`, and `.second`. For any other combination of fields, it uses calendar units like `3 months, 11 days`.

## Parameters

- `anchor`: The date the style uses to calculate the offset from the format input date.
- `allowedFields`: The units of time that may appear in the formatted output.
- `maxFieldCount`: The maximum number of units shown at once. For example, 1 hour, 34 minutes, and 23 seconds is shown as `1 hour, 34 minutes` by default, but as `1 hour` if `maxFieldCount` is set to 1.
- `sign`: The strategy for displaying a sign to signal whether the offset points toward the future or past.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/systemformatstyle/dateoffset/init(to:allowedfields:maxfieldcount:sign:))*