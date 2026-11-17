# timeZone

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The time zone in which this asset was captured.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var timeZone: TimeZone? { get }
```

```objc
@property (copy, readonly, nullable) NSTimeZone * timeZone;
```

## Discussion

Use this time zone to present [`creationDate`](../phasset/creationdate.md) in capture-local time. The time zone comes from the original file’s metadata (its time offset or GPS location), or from a time zone the user or an app set. If no capture time zone is known, it’s the device’s time zone when the asset was added to the library. The value is `nil` if the library doesn’t record a time zone for the asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetextendedmetadata/timezone)*