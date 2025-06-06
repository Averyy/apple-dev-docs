# exportsItemProviders(_:onExport:onEdit:)

**Framework**: SwiftUI  
**Kind**: method

Exports a read-write item provider for consumption by shortcuts, quick actions, and services.

**Availability**:
- macOS 12.0+

## Declaration

```swift
nonisolated
func exportsItemProviders(_ contentTypes: [UTType], onExport: @escaping () -> [NSItemProvider], onEdit: @escaping ([NSItemProvider]) -> Bool) -> some View
```

#### Discussion

If the associated view supports selection, the exported item should reflect that selected subpart.

## Parameters

- `contentTypes`: The types of content that the view supports exporting   and importing. An empty array means the view does not currently   support exporting.
- `onExport`: A closure that will be called on request of the items   by the shortcut or service.
- `onEdit`: A closure that will be called after the shortcut or   service completes with its output data. This should replace the   selected subpart that was exported with  . Return   to   indicate that there was a failure to receive the items.

## See Also

- [func importsItemProviders([UTType], onImport: ([NSItemProvider]) -> Bool) -> some View](view/importsitemproviders(_:onimport:).md)
  Enables importing item providers from services, such as Continuity Camera on macOS.
- [func exportsItemProviders([UTType], onExport: () -> [NSItemProvider]) -> some View](view/exportsitemproviders(_:onexport:).md)
  Exports a read-only item provider for consumption by shortcuts, quick actions, and services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/exportsitemproviders(_:onexport:onedit:))*