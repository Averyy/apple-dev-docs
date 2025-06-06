# setPreservationPriority(_:forTags:)

**Framework**: Foundation  
**Kind**: method

A hint to the system of the relative order for purging tagged sets of resources in the bundle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func setPreservationPriority(_ priority: Double, forTags tags: Set<String>)
```

## Parameters

- `priority`: Possible values are between   and  . The default is  . The system will attempt to purge resources with lower priorities first.
- `tags`: A set of tag names specifying resources stored in the bundle. Must not be  . An exception is thrown if any of the tags in the set do not exist in your app.

## See Also

- [func preservationPriority(forTag: String) -> Double](bundle/preservationpriority(fortag:).md)
  Returns the current preservation priority for the specified tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/setpreservationpriority(_:fortags:))*