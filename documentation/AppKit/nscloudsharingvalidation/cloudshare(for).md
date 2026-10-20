# cloudShare(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the Cloud share object that corresponds to the specified item, if one exists.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
func cloudShare(for item: any NSValidatedUserInterfaceItem) -> CKShare?
```

```objc
- (CKShare *) cloudShareForUserInterfaceItem:(id<NSValidatedUserInterfaceItem>) item;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscloudsharingvalidation/cloudshare(for:))*