# redacted(reason:)

**Framework**: PermissionKit  
**Kind**: method

Adds a reason to apply a redaction to this view hierarchy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 26.0+ (Beta)
- watchOS 7.0+

## Declaration

```swift
nonisolated
func redacted(reason: RedactionReasons) -> some View
```

#### Discussion

Adding a redaction is an additive process: any redaction provided will be added to the reasons provided by the parent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/redacted(reason:))*