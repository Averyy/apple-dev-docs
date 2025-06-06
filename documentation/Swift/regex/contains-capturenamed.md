# contains(captureNamed:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether a named capture with the given name exists.

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
func contains(captureNamed name: String) -> Bool
```

#### Discussion

This example shows a regular expression that includes capture groups named `key` and `value`:

```swift
let regex = try Regex("(?'key'.+?): (?'value'.+)")
regex.contains(captureNamed: "key")       // true
regex.contains(captureNamed: "VALUE")     // false
regex.contains(captureNamed: "1")         // false
```

## Parameters

- `name`: The name to look for among the regular expression’s   capture groups. Capture group names are case sensitive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/contains(capturenamed:))*