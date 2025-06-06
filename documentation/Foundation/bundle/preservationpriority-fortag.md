# preservationPriority(forTag:)

**Framework**: Foundation  
**Kind**: method

Returns the current preservation priority for the specified tag.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func preservationPriority(forTag tag: String) -> Double
```

#### Return Value

The preservation priority for the specified `tag`. Possible values are between `0.0` and `1.0`

## Parameters

- `tag`: A string specifying the identifier for a group of related resources. An exception is thrown if   does not exist in your app.

## See Also

- [func setPreservationPriority(Double, forTags: Set<String>)](bundle/setpreservationpriority(_:fortags:).md)
  A hint to the system of the relative order for purging tagged sets of resources in the bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/preservationpriority(fortag:))*