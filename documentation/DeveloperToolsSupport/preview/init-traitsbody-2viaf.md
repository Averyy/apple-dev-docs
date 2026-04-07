# init(_:traits:body:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a preview of an NSViewController.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
init(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., body: @escaping @MainActor () -> NSViewController)
```

#### Discussion

The `#Preview` macro expands into a declaration that calls this initializer. To create a preview that appears in the canvas, you must use the macro, not call this initializer directly.

## See Also

- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSView)](preview/init(_:traits:body:)-158mk.md)
  Creates a preview of an NSView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:traits:body:)-2viaf)*