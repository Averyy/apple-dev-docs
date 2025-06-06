# init(to:allowedFields:maxFieldCount:thresholdField:)

**Framework**: SwiftUI  
**Kind**: init

Create a format style to refer to a date in the most natural way.

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
- `allowedFields`: The units of time that may be used in the format   to express the reference. The   is always assumed   to be allowed.
- `maxFieldCount`: The number of fields that can be shown at once   when   using an abolute format. For example, January 9, 2007 is   shown as   by default, but as   if   the   is set to three. The style automatically   excludes more significant fields if their value is equal to the   value in the reference date and they are not necessary for the   format pattern, making room for less significant fields.
- `thresholdField`: The least precise field preserving which   warrants increasing the field count from one, i.e. switching from   the relative   to the absolute representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/systemformatstyle/datereference/init(to:allowedfields:maxfieldcount:thresholdfield:))*