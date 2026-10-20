# exportsItemProviders(_:onExport:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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

- `contentTypes`: The types of content that the view supports exporting. An empty array means the view does not currently support exporting.
- `onExport`: A closure that will be called on request of the items by the shortcut or service.

## See Also

### Importing and exporting using item providers
- [func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) -> some View](./importsitemproviders%28_,onimport%29.md)
  Enables importing item providers from services, such as Continuity Camera on macOS.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider], onEdit: ([NSItemProvider]) -> Bool) -> some View](./exportsitemproviders%28_,onexport,onedit%29.md)
  Exports a read-write item provider for consumption by shortcuts, quick actions, and services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/exportsitemproviders(_:onexport:))*