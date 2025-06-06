# content

**Framework**: DeviceActivity  
**Kind**: property  
**Required**: Yes

A closure that builds your report’s content with the provided configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
@ViewBuilder
var content: (Self.Configuration) -> Self.Content { get }
```

#### Discussion

Use this closure to update your scene’s content when your app changes the filter for a report or the system fetches more device activity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreportscene/content-swift.property)*