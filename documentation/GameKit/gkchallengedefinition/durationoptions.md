# durationOptions

**Framework**: GameKit  
**Kind**: property

The duration options for the challenge, like `1 day` or `1 week`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var durationOptions: [DateComponents] { get }
```

#### Discussion

> **Note**: If set, the amount of weeks is stored in the `weekOfYear` field.

> ❗ **Important**: The actual duration of the challenge may be dynamically adjusted in order to accommodate different factors like players’ timezones.

## See Also

- [var isRepeatable: Bool](gkchallengedefinition/isrepeatable.md)
  Indicates if a challenge can be attempted more than once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengedefinition/durationoptions)*