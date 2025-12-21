# init(_:widget:relevanceEntries:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a preview of a relevance-driven widget.

**Availability**:
- watchOS 26.0+

## Declaration

```swift
@MainActor
init<Entry>(_ name: String? = nil, widget: @escaping () -> some Widget, @PreviewRelevanceEntryBuilder<Entry> relevanceEntries: @escaping @MainActor () async -> [Entry]) where Entry : RelevanceEntry
```

#### Discussion

The `#Preview` macro expands into a declaration that calls this initializer. To create a preview that appears in the canvas, you must use the macro, not instantiate a Preview directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:widget:relevanceentries:))*