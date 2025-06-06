# subscript(_:)

**Framework**: UIKit  
**Kind**: subscript  
**Required**: Yes

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
subscript<T>(trait: T.Type) -> T.Value where T : UITraitDefinition, T.Value : RawRepresentable, T.Value.RawValue == Double { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimutabletraits-13ja5/subscript(_:)-ve6h)*