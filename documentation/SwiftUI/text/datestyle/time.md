# time

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

A style displaying only the time component for a date.

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
static let time: Text.DateStyle
```

#### Discussion

```swift
Text(event.startDate, style: .time)
```

Example output: 11:23PM

## See Also

### Getting text date styles
- [static let date: Text.DateStyle](./date.md)
  A style displaying a date.
- [static let offset: Text.DateStyle](./offset.md)
  A style displaying a date as offset from now.
- [static let relative: Text.DateStyle](./relative.md)
  A style displaying a date as relative to now.
- [static let timer: Text.DateStyle](./timer.md)
  A style displaying a date as timer counting from now.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/datestyle/time)*