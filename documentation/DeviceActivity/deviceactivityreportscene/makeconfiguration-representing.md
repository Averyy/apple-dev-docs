# makeConfiguration(representing:)

**Framework**: DeviceActivity  
**Kind**: method  
**Required**: Yes

Creates a new configuration that represents the provided data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
func makeConfiguration(representing data: DeviceActivityResults<DeviceActivityData>) async -> Self.Configuration
```

#### Discussion

Use this function to create a new configuration when your app changes the filter for a report or the system fetches more device activity data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreportscene/makeconfiguration(representing:))*