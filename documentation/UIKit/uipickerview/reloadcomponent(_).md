# reloadComponent(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reloads a particular component of the picker view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func reloadComponent(_ component: Int)
```

```objc
- (void) reloadComponent:(NSInteger) component;
```

## Discussion

Calling this method causes the picker view to query the delegate for new data for the given component.

## Parameters

- `component`: A zero-indexed number identifying a component of the picker view.

## See Also

### Reloading the picker view
- [func reloadAllComponents()](./reloadallcomponents%28%29.md)
  Reloads all components of the picker view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipickerview/reloadcomponent(_:))*