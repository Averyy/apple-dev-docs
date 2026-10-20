# ENDetectExposuresHandler

**Framework**: Exposure Notification  
**Kind**: typealias  
**Role**: Type Alias

The definition of a handler that returns exposure summaries.

**Availability**:
- iOS 12.5+ - Deprecated in 27.0
- iPadOS 12.5+ - Deprecated in 27.0
- Mac Catalyst 12.5+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
typealias ENDetectExposuresHandler = (ENExposureDetectionSummary?, (any Error)?) -> Void
```

```c
typedef void (^)(ENExposureDetectionSummary *, NSError *) ENDetectExposuresHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/endetectexposureshandler)*