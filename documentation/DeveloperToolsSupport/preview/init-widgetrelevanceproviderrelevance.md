# init(_:widget:relevanceProvider:relevance:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a preview of a relevance-driven widget.

**Availability**:
- watchOS 26.0+

## Declaration

```swift
@MainActor
init<Provider>(_ name: String? = nil, widget: @escaping @MainActor () -> some Widget, relevanceProvider: @escaping @MainActor () -> Provider, relevance: @escaping @MainActor () async -> WidgetRelevance<Provider.Configuration>) where Provider : RelevanceEntriesProvider
```

#### Discussion

The `#Preview` macro expands into a declaration that calls this initializer. To create a preview that appears in the canvas, you must use the macro, not instantiate a Preview directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:widget:relevanceprovider:relevance:))*