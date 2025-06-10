# init(_:strategy:)

**Framework**: Foundation  
**Kind**: init

Creates a new `DateComponents` by parsing the given string representation.

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
init<T, Value>(_ value: Value, strategy: T) throws where T : ParseStrategy, Value : StringProtocol, T.ParseInput == String, T.ParseOutput == DateComponents
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponents/init(_:strategy:)-62hv8)*