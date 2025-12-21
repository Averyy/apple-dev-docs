# init(appExtensionPoint:)

**Framework**: ExtensionFoundation  
**Kind**: init

Creates a new monitor and configures it with the specified extension point.

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
convenience init(appExtensionPoint: AppExtensionPoint) async throws
```

#### Discussion

Use this initializer to create a monitor and start looking for app extensions that match the specified extension point. This initializer returns after successfully adding the extension point to the monitor and generating the initial list of app extensions.

## Parameters

- `appExtensionPoint`: An extension point type you defined in your host app.

## See Also

- [init()](appextensionpoint/monitor/init.md)
  Creates a new monitor without any extension points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/monitor/init(appextensionpoint:))*