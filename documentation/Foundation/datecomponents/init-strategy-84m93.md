# init(_:strategy:)

**Framework**: Foundation  
**Kind**: init

Creates a new `DateComponents` by parsing the given representation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
init<T>(_ value: T.ParseInput, strategy: T) throws where T : ParseStrategy, T.ParseOutput == DateComponents
```

## Parameters

- `value`: A representation of a date. The type of the representation is specified by  .
- `strategy`: The parse strategy to parse   whose   is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/init(_:strategy:)-84m93)*