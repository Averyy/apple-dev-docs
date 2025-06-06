# DeviceActivityReportExtension

**Framework**: DeviceActivity  
**Kind**: protocol

An app extension that reports device activity data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
protocol DeviceActivityReportExtension : AppExtension
```

#### Overview

Your extension is provided with the data that your app requests when it instantiates a `DeviceActivityReport`, which it uses to render a [`View`](https://developer.apple.com/documentation/SwiftUI/View) representing the user’s device activity.

## Topics

### Associated Types
- [associatedtype Body : DeviceActivityReportScene](deviceactivityreportextension/body-swift.associatedtype.md)
  The body of the extension’s scene.
### Instance Properties
- [var body: Self.Body](deviceactivityreportextension/body-swift.property.md)
  A body containing a [`DeviceActivityReportScene`](deviceactivityreportscene.md) for each context that your extension supports.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityreportextension)*