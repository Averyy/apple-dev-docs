# exportsItemProviders(_:onExport:)

**Framework**: PermissionKit  
**Kind**: method

Exports a read-only item provider for consumption by shortcuts, quick actions, and services.

**Availability**:
- macOS 12.0+

## Declaration

```swift
nonisolated
func exportsItemProviders(_ contentTypes: [UTType], onExport: @escaping () -> [NSItemProvider]) -> some View
```

#### Discussion

If the associated view supports selection, the exported item should reflect that selected subpart.

## Parameters

- `contentTypes`: The types of content that the view supports exporting.   An empty array means the view does not currently support exporting.
- `onExport`: A closure that will be called on request of the items   by the shortcut or service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/exportsitemproviders(_:onexport:))*