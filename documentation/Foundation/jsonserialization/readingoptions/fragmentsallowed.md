# fragmentsAllowed

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that the parser allows top-level objects that aren’t arrays or dictionaries.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var fragmentsAllowed: JSONSerialization.ReadingOptions { get }
```

```c
NSJSONReadingFragmentsAllowed
```

## See Also

### Reading Options
- [static var mutableContainers: JSONSerialization.ReadingOptions](./mutablecontainers.md)
  Specifies that arrays and dictionaries in the returned object are mutable.
- [static var mutableLeaves: JSONSerialization.ReadingOptions](./mutableleaves.md)
  Specifies that leaf strings in the JSON object graph are mutable.
- [static var json5Allowed: JSONSerialization.ReadingOptions](./json5allowed.md)
  Specifies that reading serialized JSON data supports the JSON5 syntax.
- [static var topLevelDictionaryAssumed: JSONSerialization.ReadingOptions](./topleveldictionaryassumed.md)
  Specifies that the parser assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with curly braces.
- [static var allowFragments: JSONSerialization.ReadingOptions](./allowfragments.md)
  A deprecated option that specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/readingoptions/fragmentsallowed)*