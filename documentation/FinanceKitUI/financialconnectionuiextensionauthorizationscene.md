# FinancialConnectionUIExtensionAuthorizationScene

**Framework**: FinanceKitUI  
**Kind**: struct  
**Role**: Structure

Implement this scene to authorize your app’s Financial Connection

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
@MainActor
@preconcurrency struct FinancialConnectionUIExtensionAuthorizationScene<Content> where Content : View
```

## Overview

Your scene will be provided a `FinancialConnectionExtensionAuthorizationRequest`. Use this request to query parameters necessary for authentication, and callback when complete.

## Topics

### Initializers
- [init(content: () -> Content)](./financialconnectionuiextensionauthorizationscene/init%28content%29.md)

## Relationships

### Conforms To
- [AppExtensionScene](../ExtensionKit/appextensionscene.md)
- [FinancialConnectionUIExtensionScene](./financialconnectionuiextensionscene.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/financialconnectionuiextensionauthorizationscene)*