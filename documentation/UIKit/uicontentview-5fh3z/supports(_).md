# supports(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Determines whether the view is compatible with the provided configuration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS

## Declaration

```swift
@MainActor
func supports(_ configuration: any UIContentConfiguration) -> Bool
```

## Return Value

[`true`](../../Swift/true.md) if the view supports this configuration being set to its [`configuration`](./configuration.md) property and is capable of updating itself for the configuration; otherwise, [`false`](../../Swift/false.md).

## Discussion

The default implementation assumes the view is compatible with configuration types that match the type of the view’s existing configuration.

## Parameters

- `configuration`: The new configuration to test for compatibility.

## Default Implementations

### UIContentView Implementations
- [func supports(any UIContentConfiguration) -> Bool](./supports%28_%29-q5rd.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontentview-5fh3z/supports(_:))*