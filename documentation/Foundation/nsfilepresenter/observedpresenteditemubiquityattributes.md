# observedPresentedItemUbiquityAttributes

**Framework**: Foundation  
**Kind**: property

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

#### Discussion

Valid attributes include the [`isUbiquitousItemKey`](urlresourcekey/isubiquitousitemkey.md) attribute and any attribute whose name starts with `ubiquitousItem` or `ubiquitousSharedItem` (or `NSURLUbiquitousItem` or `NSURLUbiquitousSharedItem` in Objective-C).

If the property is not implemented, the system generates notifications for all the ubiquity attributes.

The system checks this property only when the file coordinator’s [`addFilePresenter(_:)`](nsfilecoordinator/addfilepresenter(_:).md) method is called. Make all changes to this property before calling [`addFilePresenter(_:)`](nsfilecoordinator/addfilepresenter(_:).md).

## See Also

- [func presentedItemDidChangeUbiquityAttributes(Set<URLResourceKey>)](nsfilepresenter/presenteditemdidchangeubiquityattributes(_:).md)
  Tells your object that the file or file package’s ubiquity attributes have changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilepresenter/observedpresenteditemubiquityattributes)*