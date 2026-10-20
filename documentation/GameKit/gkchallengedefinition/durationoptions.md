# durationOptions

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The duration options for the challenge, like `1 day` or `1 week`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var durationOptions: [DateComponents] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<NSDateComponents *> * durationOptions;
```

#### Discussion

> **Note**: If set, the amount of weeks is stored in the `weekOfYear` field.

> ❗ **Important**: The actual duration of the challenge may be dynamically adjusted in order to accommodate different factors like players’ timezones.

## See Also

### Getting the challenge rules
- [var isRepeatable: Bool](./isrepeatable.md)
  Indicates if a challenge can be attempted more than once.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengedefinition/durationoptions)*