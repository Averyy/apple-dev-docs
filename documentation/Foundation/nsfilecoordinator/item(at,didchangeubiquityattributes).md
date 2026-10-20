# item(at:didChangeUbiquityAttributes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells observing file providers that the item’s ubiquity attributes have changed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func item(at url: URL, didChangeUbiquityAttributes attributes: Set<URLResourceKey>)
```

```objc
- (void) itemAtURL:(NSURL *) url didChangeUbiquityAttributes:(NSSet<NSString *> *) attributes;
```

#### Discussion

This method triggers the [NSFilePresenter](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_6) protocol’s [`presentedItemDidChangeUbiquityAttributes(_:)`](../nsfilepresenter/presenteditemdidchangeubiquityattributes%28_%29.md) method on any file presenters that are observing the item, even if they are running in different processes.

For information about the types of attributes that can trigger notifications, see the [`NSFilePresenter`](../nsfilepresenter.md) protocol’s [`observedPresentedItemUbiquityAttributes`](../nsfilepresenter/observedpresenteditemubiquityattributes.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilecoordinator/item(at:didchangeubiquityattributes:))*