# supports(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Determines whether the view is compatible with the provided configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
@MainActor
func supports(_ configuration: any UIContentConfiguration) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the view supports this configuration being set to its [`configuration`](uicontentview-5fh3z/configuration.md) property and is capable of updating itself for the configuration; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The default implementation assumes the view is compatible with configuration types that match the type of the view’s existing configuration.

## Parameters

- `configuration`: The new configuration to test for compatibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentview-5fh3z/supports(_:))*