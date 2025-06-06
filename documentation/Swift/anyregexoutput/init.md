# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a dynamic regular expression match output from an existing match.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init<Output>(_ match: Regex<Output>.Match)
```

#### Discussion

You can use this initializer when you need an `AnyRegexOutput` instance instead of the output type of a strongly-typed `Regex.Match`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyregexoutput/init(_:))*