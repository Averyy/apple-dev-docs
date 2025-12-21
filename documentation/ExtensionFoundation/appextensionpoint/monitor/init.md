# init()

**Framework**: ExtensionFoundation  
**Kind**: init

Creates a new monitor without any extension points.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
init()
```

#### Discussion

After using this initializer, call the [`addAppExtensionPoint(_:)`](appextensionpoint/monitor/addappextensionpoint(_:).md) method to add an extension point to monitor.

## See Also

- [convenience init(appExtensionPoint: AppExtensionPoint) async throws](appextensionpoint/monitor/init(appextensionpoint:).md)
  Creates a new monitor and configures it with the specified extension point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/init())*