# init(bundleIdentifier:)

**Framework**: Screen Time  
**Kind**: init

Creates a web history instance to delete web-usage data associated to the bundle identifier you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
init(bundleIdentifier: String) throws
```

#### Discussion

The default value for `bundleIdentifier` is `Bundle.main.bundleIdentifier`. This is the recommended identifier to use, except for example, if a helper process is presenting web UI and you want to group that web-usage under the main app’s bundle identifier.

## Parameters

- `bundleIdentifier`: The bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screentime/stwebhistory/init(bundleidentifier:))*