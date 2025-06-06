# wholeMatch(in:)

**Framework**: Swift  
**Kind**: method

Returns a match if this regex matches the given string in its entirety.

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
func wholeMatch(in string: String) throws -> Regex<Output>.Match?
```

#### Return Value

The match, if this regex matches the entirety of `string`; otherwise, `nil`.

#### Discussion

Call this method if you want the regular expression to succeed only when it matches the entire string you pass as `string`. The following example shows matching a regular expression that only matches digits, with different candidate strings.

```swift
let digits = /[0-9]+/

if let digitsMatch = try digits.wholeMatch(in: "2022") {
    print(digitsMatch.0)
} else {
    print("No match.")
}
// Prints "2022"

if let digitsMatch = try digits.wholeMatch(in: "The year is 2022.") {
    print(digitsMatch.0)
} else {
    print("No match.")
}
// Prints "No match."
```

The `wholeMatch(in:)` method can throw an error if this regex includes a transformation closure that throws an error.

## Parameters

- `string`: The string to match this regular expression against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/wholematch(in:)-9do8t)*