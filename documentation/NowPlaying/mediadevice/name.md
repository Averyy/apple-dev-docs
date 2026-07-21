# name

**Framework**: Now Playing  
**Kind**: property

The human-readable name of the device.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
let name: String
```

#### Discussion

The system displays this name in the Now Playing interface. Use a descriptive name that helps people identify the device.

The name must be non-empty and at most 250 characters. It must start with an alphanumeric character, end with an alphanumeric character or `.`, and otherwise contain only alphanumerics, whitespace, and the punctuation `' - , & # .`. Symbols outside this set — including emoji and SF Symbols — are not permitted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediadevice/name)*