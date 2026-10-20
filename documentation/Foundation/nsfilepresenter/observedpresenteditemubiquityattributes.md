# observedPresentedItemUbiquityAttributes

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A list of ubiquity attributes used to generate and send notifications whenever an attribute in the list changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
optional var observedPresentedItemUbiquityAttributes: Set<URLResourceKey> { get }
```

```objc
@property (strong, readonly) NSSet<NSString *> * observedPresentedItemUbiquityAttributes;
```

#### Discussion

Valid attributes include the [`isUbiquitousItemKey`](../urlresourcekey/isubiquitousitemkey.md) attribute and any attribute whose name starts with `ubiquitousItem` or `ubiquitousSharedItem` (or `NSURLUbiquitousItem` or `NSURLUbiquitousSharedItem` in Objective-C).

If the property is not implemented, the system generates notifications for all the ubiquity attributes.

The system checks this property only when the file coordinator’s [`addFilePresenter(_:)`](../nsfilecoordinator/addfilepresenter%28_%29.md) method is called. Make all changes to this property before calling [`addFilePresenter(_:)`](../nsfilecoordinator/addfilepresenter%28_%29.md).

## See Also

### Ubiquity Change Notifications
- [func presentedItemDidChangeUbiquityAttributes(Set<URLResourceKey>)](./presenteditemdidchangeubiquityattributes%28_%29.md)
  Tells your object that the file or file package’s ubiquity attributes have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/observedpresenteditemubiquityattributes)*