# makeBody(configuration:)

**Framework**: SwiftUI  
**Kind**: method  
**Required**: Yes

Returns the appearance and interaction content for a `DatePicker`.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@ViewBuilder
@MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

#### Discussion

The system calls this method for each [`DatePicker`](datepicker.md) instance in a view hierarchy where this style is the current date picker style.

## See Also

- [struct DatePickerStyleConfiguration](datepickerstyleconfiguration.md)
  The properties of a `DatePicker`.
- [DatePickerStyle.Configuration](datepickerstyle/configuration.md)
  A type alias for the properties of a `DatePicker`.
- [associatedtype Body : View](datepickerstyle/body.md)
  A view representing the appearance and interaction of a `DatePicker`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/datepickerstyle/makebody(configuration:))*