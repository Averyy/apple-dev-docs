# error

**Framework**: StoreKit  
**Kind**: property

The error value that indicates the reason a promotional image failed to load.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var error: (any Error)? { get }
```

#### Discussion

The [`error`](producticonphase/error.md) value is `nil` while the icon is loading, if the icon successfully loads, or if you haven’t set up a promotional image for the in-app purchase in App Store Connect. Use this value as a convenience to access the error value in code that assumes you’ve set up a promotional image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/producticonphase/error)*