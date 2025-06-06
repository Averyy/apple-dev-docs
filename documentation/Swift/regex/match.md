# Regex.Match

**Framework**: Swift  
**Kind**: struct

The result of matching a regular expression against a string.

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
@dynamicMemberLookup
struct Match
```

#### Overview

A `Match` forwards API to the `Output` generic parameter, providing direct access to captures.

## Topics

### Initializers
- [init<OtherOutput>(Regex<OtherOutput>.Match)](regex/match/init(_:).md)
  Creates a regular expression match with a dynamic capture list from the given match.
### Instance Properties
- [var output: Output](regex/match/output.md)
  The output produced from the match operation.
- [let range: Range<String.Index>](regex/match/range.md)
  The range of the overall match.
### Subscripts
- [subscript(String) -> AnyRegexOutput.Element?](regex/match/subscript(_:)-9bzv4.md)
  Accesses the capture with the specified name, if a capture with that name exists.
- [subscript<Capture>(Reference<Capture>) -> Capture](regex/match/subscript(_:)-vbin.md)
  Accesses this match’s capture by the given reference.
- [subscript<T>(dynamicMember _: KeyPath<Output, T>) -> T](regex/match/subscript(dynamicmember:).md)
  Accesses a capture by its name or number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/match)*