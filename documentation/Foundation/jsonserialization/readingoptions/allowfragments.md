# allowFragments

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A deprecated option that specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2 (renamed: JSONSerialization.ReadingOptions.fragmentsAllowed)
- iPadOS 5.0+ - Deprecated in 27.2 (renamed: JSONSerialization.ReadingOptions.fragmentsAllowed)
- Mac Catalyst 13.1+ - Deprecated in 27.2 (renamed: JSONSerialization.ReadingOptions.fragmentsAllowed)
- macOS 10.7+ - Deprecated in 27.2 (renamed: JSONSerialization.ReadingOptions.fragmentsAllowed)
- tvOS 9.0+ - Deprecated in 27.2 (renamed: JSONSerialization.ReadingOptions.fragmentsAllowed)
- visionOS 1.0+ - Deprecated in 27.2 (renamed: JSONSerialization.ReadingOptions.fragmentsAllowed)
- watchOS 2.0+ - Deprecated in 27.2 (renamed: JSONSerialization.ReadingOptions.fragmentsAllowed)

> **Deprecated**: Use [`fragmentsAllowed`](./fragmentsallowed.md) instead.

## Declaration

```swift
static var allowFragments: JSONSerialization.ReadingOptions { get }
```

```c
NSJSONReadingAllowFragments
```

## See Also

### Reading Options
- [static var mutableContainers: JSONSerialization.ReadingOptions](./mutablecontainers.md)
  Specifies that arrays and dictionaries in the returned object are mutable.
- [static var mutableLeaves: JSONSerialization.ReadingOptions](./mutableleaves.md)
  Specifies that leaf strings in the JSON object graph are mutable.
- [static var fragmentsAllowed: JSONSerialization.ReadingOptions](./fragmentsallowed.md)
  Specifies that the parser allows top-level objects that aren’t arrays or dictionaries.
- [static var json5Allowed: JSONSerialization.ReadingOptions](./json5allowed.md)
  Specifies that reading serialized JSON data supports the JSON5 syntax.
- [static var topLevelDictionaryAssumed: JSONSerialization.ReadingOptions](./topleveldictionaryassumed.md)
  Specifies that the parser assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with curly braces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/readingoptions/allowfragments)*