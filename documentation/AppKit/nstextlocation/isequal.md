# isEqual(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns `true` for locations representing the same document position.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func isEqual(_ location: Any?) -> Bool
```

#### Discussion

Must not depend on auxiliary state such as affinity or visual-edge preference. Locations from different data source methods are compared using `isEqual:` and must agree when they refer to the same position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlocation/isequal(_:))*