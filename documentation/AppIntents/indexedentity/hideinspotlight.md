# hideInSpotlight

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether Spotlight prevents the inclusion of the entity in the index.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
var hideInSpotlight: Bool { get }
```

#### Discussion

When the value of this property is `true`, Spotlight doesn’t include the entity in search results. The default value of this property is `false`.

## Default Implementations

### IndexedEntity Implementations
- [var hideInSpotlight: Bool](./hideinspotlight-7sp5n.md)
  A Boolean value that indicates whether Spotlight prevents the inclusion of the entity in the index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/indexedentity/hideinspotlight)*