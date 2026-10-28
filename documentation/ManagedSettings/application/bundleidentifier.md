# bundleIdentifier

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Instance Property

The unique string that identifies this app.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
let bundleIdentifier: String?
```

## Discussion

In an extension that provides shield configurations, this property provides the app’s bundle identifier. When you access this property outside that extension, the value is `nil`. See `ShieldConfigurationDataSource` in the `ManagedSettingsUI` framework for more information.

## See Also

### Accessing application information
- [let token: ApplicationToken?](./token.md)
  An opaque representation of a specific web domain.
- [let localizedDisplayName: String?](./localizeddisplayname.md)
  A localized display name for the application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/application/bundleidentifier)*