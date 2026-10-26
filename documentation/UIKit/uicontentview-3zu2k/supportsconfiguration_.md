# supportsConfiguration:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Determines whether the view is compatible with the provided configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (BOOL) supportsConfiguration:(id<UIContentConfiguration>) configuration;
```

#### Return Value

[`true`](../../Swift/true.md) if the view supports this configuration being set to its [`configuration`](./configuration.md) property and is capable of updating itself for the configuration; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The default implementation assumes the view is compatible with configuration classes that match the class of the view’s existing configuration.

## Parameters

- `configuration`: The new configuration to test for compatibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentview-3zu2k/supportsconfiguration:)*