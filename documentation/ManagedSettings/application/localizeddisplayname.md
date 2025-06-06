# localizedDisplayName

**Framework**: ManagedSettings  
**Kind**: property

A localized display name for the application.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
let localizedDisplayName: String?
```

#### Discussion

In an extension that provides shield configurations, this property provides the app’s name. When you access this property outside that extension, the value is `nil`. See `ShieldConfigurationDataSource` in the Managed Settings UI framework for more information.

## See Also

- [let bundleIdentifier: String?](application/bundleidentifier.md)
  The unique string that identifies this app.
- [let token: ApplicationToken?](application/token.md)
  An opaque representation of a specific web domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/application/localizeddisplayname)*