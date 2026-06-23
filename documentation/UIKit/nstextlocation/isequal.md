# isEqual(_:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Returns `true` for locations representing the same document position.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func isEqual(_ location: Any?) -> Bool
```

#### Discussion

Must not depend on auxiliary state such as affinity or visual-edge preference. Locations from different data source methods are compared using `isEqual:` and must agree when they refer to the same position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextlocation/isequal(_:))*