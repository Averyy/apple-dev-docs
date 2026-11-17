# timeZone

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

The time zone in which the asset was captured.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
var timeZone: TimeZone? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSTimeZone * timeZone;
```

## Discussion

The time zone applies to the asset’s [`creationDate`](../phasset/creationdate.md), including a creation date set in the same change request. Set to `nil` to restore the time zone Photos derives from the asset’s original metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetchangerequest/timezone)*