# init(to:allowedFields:maxFieldCount:thresholdField:)

**Framework**: SwiftUI  
**Kind**: init

Creates a format style that refers to a comparison date using natural language.

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
init(to date: Date, allowedFields: Set<Date.RelativeFormatStyle.Field> = [.year, .month, .day, .hour, .minute], maxFieldCount: Int = 2, thresholdField: Date.RelativeFormatStyle.Field = .day)
```

## Parameters

- `date`: The date this format references.
- `allowedFields`: The units of time that may appear in the relative representation. The style always includes the `thresholdField` regardless of this set.
- `maxFieldCount`: The maximum number of fields the style shows in the absolute representation. The style excludes more significant fields whose value matches the reference date, making room for less significant ones.
- `thresholdField`: The time unit that tells the style when to switch from relative to absolute representation. For example, if you provide `.minute` and the time difference extends to hours or days, the style switches from relative to absolute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/systemformatstyle/datereference/init(to:allowedfields:maxfieldcount:thresholdfield:))*