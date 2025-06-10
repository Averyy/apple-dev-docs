# filter(runBoundaries:)

**Framework**: Foundation  
**Kind**: method

Returns an attribute container storing only the attributes in `self` with a matching run boundary property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
func filter(runBoundaries: AttributedString.AttributeRunBoundaries?) -> AttributeContainer
```

#### Discussion

Note: if `nil` is provided then only attributes not bound to any particular boundary will be returned


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributecontainer/filter(runboundaries:))*