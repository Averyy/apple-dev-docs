# init(_:traits:arguments:body:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a group of previews of a SwiftUI view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 27.0+ (Beta)
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@MainActor
init<T>(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], @ContentBuilder body: @escaping @MainActor (T) -> any View)
```

#### Discussion

A preview macro expands into a declaration that calls this initializer. Don’t use this initializer directly.

## Parameters

- `name`: An optional display name for the preview.
- `traits`: An optional list of traits to customize the preview.
- `arguments`: An array of arguments to pass into `body`.
- `body`: A closure that maps an argument to a SwiftUI view to preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:traits:arguments:body:)-1xqo1)*