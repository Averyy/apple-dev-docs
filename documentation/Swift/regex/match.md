# Regex.Match

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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
- [init<OtherOutput>(Regex<OtherOutput>.Match)](./match/init%28_%29.md)
  Creates a regular expression match with a dynamic capture list from the given match.
### Instance Properties
- [var output: Output](./match/output.md)
  The output produced from the match operation.
- [let range: Range<String.Index>](./match/range.md)
  The range of the overall match.
### Subscripts
- [subscript(String) -> AnyRegexOutput.Element?](./match/subscript%28_%29-9bzv4.md)
  Accesses the capture with the specified name, if a capture with that name exists.
- [subscript<Capture>(Reference<Capture>) -> Capture](./match/subscript%28_%29-vbin.md)
  Accesses this match’s capture by the given reference.
- [subscript<T>(dynamicMember _: KeyPath<Output, T>) -> T](./match/subscript%28dynamicmember%29.md)
  Accesses a capture by its name or number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/regex/match)*