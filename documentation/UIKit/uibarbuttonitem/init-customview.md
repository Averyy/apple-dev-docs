# init(customView:)

**Framework**: UIKit  
**Kind**: init

Creates an item using the specified custom view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(customView: UIView)
```

#### Return Value

A newly initialized [`UIBarButtonItem`](uibarbuttonitem.md).

#### Discussion

The bar button item created by this method doesn’t call the action method of its target in response to user interactions. Instead, the bar button item expects the specified custom view to handle any user interactions and provide an appropriate response.

## Parameters

- `customView`: A custom view representing the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitem/init(customview:))*