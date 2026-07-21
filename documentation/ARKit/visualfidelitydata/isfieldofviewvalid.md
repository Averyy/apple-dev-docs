# isFieldOfViewValid

**Framework**: ARKit  
**Kind**: property

Indicates whether the field of view (FoV) is valid.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
var isFieldOfViewValid: Bool { get }
```

#### Discussion

Returns `true` if the expected FoV meets requirements. Returns `false` if any portion of the FoV is invalid.

Note: Returns `false` if the provider was created without a field of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/visualfidelitydata/isfieldofviewvalid)*