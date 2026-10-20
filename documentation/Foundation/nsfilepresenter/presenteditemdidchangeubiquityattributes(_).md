# presentedItemDidChangeUbiquityAttributes(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells your object that the file or file package’s ubiquity attributes have changed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
optional func presentedItemDidChangeUbiquityAttributes(_ attributes: Set<URLResourceKey>)
```

```objc
- (void) presentedItemDidChangeUbiquityAttributes:(NSSet<NSString *> *) attributes;
```

#### Discussion

To specify the ubiquity attributes that trigger notifications, implement your file provider’s [`observedPresentedItemUbiquityAttributes`](./observedpresenteditemubiquityattributes.md) property. If you do not implement this property, the system sends notifications when any ubiquity attribute changes.

> **Note**:  Changes to the ubiquity attributes don’t typically align with [`presentedItemDidChange()`](./presenteditemdidchange%28%29.md) notifications.

## Parameters

- `attributes`: The set of ubiquity attributes that have changed. For information about valid ubiquity attributes, see the [`observedPresentedItemUbiquityAttributes`](./observedpresenteditemubiquityattributes.md) property.

## See Also

### Related Documentation
- [func item(at: URL, didChangeUbiquityAttributes: Set<URLResourceKey>)](../nsfilecoordinator/item%28at,didchangeubiquityattributes%29.md)
  Tells observing file providers that the item’s ubiquity attributes have changed.
### Ubiquity Change Notifications
- [var observedPresentedItemUbiquityAttributes: Set<URLResourceKey>](./observedpresenteditemubiquityattributes.md)
  A list of ubiquity attributes used to generate and send notifications whenever an attribute in the list changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/presenteditemdidchangeubiquityattributes(_:))*