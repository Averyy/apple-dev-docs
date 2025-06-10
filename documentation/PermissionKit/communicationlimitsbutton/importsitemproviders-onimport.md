# importsItemProviders(_:onImport:)

**Framework**: PermissionKit  
**Kind**: method

Enables importing item providers from services, such as Continuity Camera on macOS.

**Availability**:
- macOS 12.0+

## Declaration

```swift
nonisolated
func importsItemProviders(_ contentTypes: [UTType], onImport: @escaping ([NSItemProvider]) -> Bool) -> some View
```

## Parameters

- `contentTypes`: The types of content that the view supports importing.   An empty array means the view does not currently support importing.
- `onImport`: A closure that will be called with the imported service   item. Return   to indicate that there was a failure to receive   the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/importsitemproviders(_:onimport:))*