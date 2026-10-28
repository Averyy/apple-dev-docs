# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an instance that displays a localized time interval.

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
init(_ interval: DateInterval)
```

**Other overloads**:

```swift
init(_ attributedContent: AttributedString)
```

```swift
init(_ dates: ClosedRange<Date>)
```

```swift
init(_ image: Image)
```

```swift
init(_ resource: LocalizedStringResource)
```

```swift
init<S>(_ content: S) where S : StringProtocol
```

## Discussion

```swift
Text(DateInterval(start: event.startDate, duration: event.duration))
```

Example output: 9:30AM - 3:30PM

## Parameters

- `interval`: The date interval to display


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/text/init(_:)-56n81)*