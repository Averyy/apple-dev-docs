# evictsObjectsWithDiscardedContent

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Whether the cache will automatically evict discardable-content objects whose content has been discarded.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var evictsObjectsWithDiscardedContent: Bool { get set }
```

```objc
@property BOOL evictsObjectsWithDiscardedContent;
```

#### Discussion

If [`true`](../../Swift/true.md), the cache will evict a discardable-content object after its content is discarded. If [`false`](../../Swift/false.md), it will not. The default value is [`true`](../../Swift/true.md).

## See Also

### Managing Discardable Content
- [protocol NSDiscardableContent](../nsdiscardablecontent.md)
  You implement this protocol when a class’s objects have subcomponents that can be discarded when not being used, thereby giving an application a smaller memory footprint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscache/evictsobjectswithdiscardedcontent)*