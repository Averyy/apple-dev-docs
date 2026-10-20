# setPreservationPriority(_:forTags:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

A hint to the system of the relative order for purging tagged sets of resources in the bundle.

**Availability**:
- iOS 9.0+ - Deprecated in 27.0
- iPadOS 9.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

> **Deprecated**: Use Background Assets instead.

## Declaration

```swift
func setPreservationPriority(_ priority: Double, forTags tags: Set<String>)
```

```objc
- (void) setPreservationPriority:(double) priority forTags:(NSSet<NSString *> *) tags;
```

## Parameters

- `priority`: A number specifying the relative priority of preserving the resources in the group specified by `tag`.

  Possible values are between `0.0` and `1.0`. The default is `0.0`. The system will attempt to purge resources with lower priorities first.
- `tags`: A set of tag names specifying resources stored in the bundle. Must not be `nil`. An exception is thrown if any of the tags in the set do not exist in your app.

## See Also

### Managing preservation priority for on-demand resources
- [func preservationPriority(forTag: String) -> Double](./preservationpriority%28fortag%29.md)
  Returns the current preservation priority for the specified tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/setpreservationpriority(_:fortags:))*