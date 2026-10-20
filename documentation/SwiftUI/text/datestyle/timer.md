# timer

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

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

### Getting text date styles
- [static let date: Text.DateStyle](./date.md)
  A style displaying a date.
- [static let offset: Text.DateStyle](./offset.md)
  A style displaying a date as offset from now.
- [static let relative: Text.DateStyle](./relative.md)
  A style displaying a date as relative to now.
- [static let time: Text.DateStyle](./time.md)
  A style displaying only the time component for a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/datestyle/timer)*