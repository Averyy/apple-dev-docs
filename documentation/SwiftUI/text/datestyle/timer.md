# timer

**Framework**: SwiftUI  
**Kind**: property

A style displaying a date as timer counting from now.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static let timer: Text.DateStyle
```

#### Discussion

```swift
Text(event.startDate, style: .timer)
```

Example output: 2:32 36:59:01

## See Also

- [static let date: Text.DateStyle](text/datestyle/date.md)
  A style displaying a date.
- [static let offset: Text.DateStyle](text/datestyle/offset.md)
  A style displaying a date as offset from now.
- [static let relative: Text.DateStyle](text/datestyle/relative.md)
  A style displaying a date as relative to now.
- [static let time: Text.DateStyle](text/datestyle/time.md)
  A style displaying only the time component for a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/datestyle/timer)*