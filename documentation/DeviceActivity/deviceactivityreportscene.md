# DeviceActivityReportScene

**Framework**: DeviceActivity  
**Kind**: protocol

Defines a custom device activity report scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
protocol DeviceActivityReportScene : AppExtensionScene
```

#### Overview

This protocol refines `AppExtensionScene` and restricts the types that can be passed to a [`DeviceActivityReportBuilder`](deviceactivityreportbuilder.md). Your extension should provide a scene for each context that your app supports.

## Topics

### Associated Types
- [associatedtype Configuration](deviceactivityreportscene/configuration.md)
  A type used to configure your scene’s [`content`](deviceactivityreportscene/content-swift.property.md).
- [associatedtype Content : View](deviceactivityreportscene/content-swift.associatedtype.md)
  The type of view that represents the scene’s content.
### Instance Properties
- [var content: (Self.Configuration) -> Self.Content](deviceactivityreportscene/content-swift.property.md)
  A closure that builds your report’s content with the provided configuration.
- [var context: DeviceActivityReport.Context](deviceactivityreportscene/context.md)
  The context of the scene.
### Instance Methods
- [func makeConfiguration(representing: DeviceActivityResults<DeviceActivityData>) async -> Self.Configuration](deviceactivityreportscene/makeconfiguration(representing:).md)
  Creates a new configuration that represents the provided data.

## Relationships

### Inherits From
- [AppExtensionScene](../ExtensionKit/AppExtensionScene.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreportscene)*