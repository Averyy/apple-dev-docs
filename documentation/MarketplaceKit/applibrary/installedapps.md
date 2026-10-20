# installedApps

**Framework**: MarketplaceKit  
**Kind**: property  
**Role**: Instance Property

The set of apps installed by the alternative app marketplace.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
final var installedApps: Set<AppLibrary.App> { get set }
```

## See Also

### Accessing installed apps
- [func app(forAppleItemID: AppleItemID) -> AppLibrary.App](./app%28forappleitemid%29.md)
  Provides the app for the given app identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/installedapps)*