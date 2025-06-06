# Label

**Framework**: Create ML Components  
**Kind**: associatedtype  
**Required**: Yes

The classification label type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
associatedtype Label : Hashable where Self.Output == ClassificationDistribution<Self.Label>
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/classifier/label)*