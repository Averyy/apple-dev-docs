# domain

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Instance Property

A string that identifies a specific web domain.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
let domain: String?
```

#### Discussion

In an extension that provides shield configurations, this property provides the web domain. When you access this property outside that extension, the value is `nil`. See [`ShieldConfigurationDataSource`](../../ManagedSettingsUI/shieldconfigurationdatasource.md) for more information.

## See Also

### Identifying a web domain
- [let token: WebDomainToken?](./token.md)
  An opaque representation of a specific web domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webdomain/domain)*