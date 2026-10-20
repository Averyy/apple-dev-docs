# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a regular expression from the given string, using a dynamic capture list.

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
init(_ pattern: String) throws
```

#### Discussion

Use this initializer to create a `Regex` instance from a regular expression that you have stored in `pattern`.

```swift
let simpleDigits = try Regex("[0-9]+")
```

This initializer throws an error if `pattern` uses invalid regular expression syntax.

The output type of the new `Regex` is the dynamic [`AnyRegexOutput`](anyregexoutput.md). If you know the capture structure of `pattern` ahead of time, use the `init(_:as:)` initializer instead.

## Parameters

- `pattern`: A string with regular expression syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/init(_:)-52kg)*