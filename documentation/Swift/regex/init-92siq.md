# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a regular expression with a dynamic capture list from the given regular expression.

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
init<OtherOutput>(_ regex: Regex<OtherOutput>)
```

#### Discussion

You can use this initializer to convert a `Regex` with strongly-typed captures into a `Regex` with `AnyRegexOutput` as its output type.

## Parameters

- `regex`: A regular expression to convert to use a dynamic   capture list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/init(_:)-92siq)*