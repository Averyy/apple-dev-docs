# init(for:)

**Framework**: UIKit  
**Kind**: init

Retrieves a focus system object that contains the state information for the specified object.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init?(for environment: any UIFocusEnvironment)
```

#### Return Value

The [`UIFocusSystem`](uifocussystem.md) object that manages the state for the specified object or `nil` if focus interactions are not available for the object.

## Parameters

- `environment`: The object whose state you want to return. Specify the view, view controller, or window whose state you want. You can also specify any other object that adopts the [`UIFocusEnvironment`](uifocusenvironment.md) protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocussystem/init(for:))*