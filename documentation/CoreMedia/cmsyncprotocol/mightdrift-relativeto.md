# mightDrift(relativeTo:)

**Framework**: Core Media  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether it’s possible for the clock to drift relative to the input.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func mightDrift<T>(relativeTo clockOrTimebase: T) -> Bool where T : CMSyncProtocol
```

## Parameters

- `clockOrTimebase`: The clock to compare to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsyncprotocol/mightdrift(relativeto:))*