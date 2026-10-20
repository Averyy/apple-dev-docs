# preservationPriority(forTag:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the current preservation priority for the specified tag.

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
func preservationPriority(forTag tag: String) -> Double
```

```objc
- (double) preservationPriorityForTag:(NSString *) tag;
```

#### Return Value

The preservation priority for the specified `tag`. Possible values are between `0.0` and `1.0`

## Parameters

- `tag`: A string specifying the identifier for a group of related resources. An exception is thrown if `tag` does not exist in your app.

## See Also

### Managing preservation priority for on-demand resources
- [func setPreservationPriority(Double, forTags: Set<String>)](./setpreservationpriority%28_,fortags%29.md)
  A hint to the system of the relative order for purging tagged sets of resources in the bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/preservationpriority(fortag:))*