# init(appex:)

**Framework**: Network Extension  
**Kind**: init

Creates a configuration for a given app extension.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init(appex: any NEURLFilterControlProvider)
```

#### Discussion

[`NEURLFilterControlProvider`](neurlfiltercontrolprovider.md) uses this method to conform to the [`ExtensionKit`](https://developer.apple.com/documentation/ExtensionKit) framework. Your extension doesn’t need to call this method directly.

## Parameters

- `appex`: The URL filter app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neurlfiltercontrolproviderconfiguration/init(appex:))*