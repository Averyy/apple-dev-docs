# init(_:strategy:)

**Framework**: Foundation  
**Kind**: init

Creates a new `DateComponents` by parsing the given representation.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init<T>(_ value: T.ParseInput, strategy: T) throws where T : ParseStrategy, T.ParseOutput == DateComponents
```

## Parameters

- `value`: A representation of a date. The type of the representation is specified by  .
- `strategy`: The parse strategy to parse   whose   is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/init(_:strategy:)-84m93)*