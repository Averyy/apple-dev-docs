# setBundleIdentifier(_:)

**Framework**: Screen Time  
**Kind**: method

Changes the bundle identifier used to report web usage.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
@MainActor
func setBundleIdentifier(_ bundleIdentifier: String) throws
```

#### Discussion

This is only supported for web browsers that have been properly registered with Screen Time.

## Parameters

- `bundleIdentifier`: The bundle identifier that can be changed to facilitate web usage   reporting for a parent web browser from one of its helper processes or extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebpagecontroller/setbundleidentifier(_:))*