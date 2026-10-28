# init(_:traits:body:)

**Framework**: DeveloperToolsSupport  
**Kind**: init  
**Role**: Initializer

Creates a preview of an NSViewController.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
init(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., body: @escaping @MainActor () -> NSViewController)
```

## Discussion

The `#Preview` macro expands into a declaration that calls this initializer. To create a preview that appears in the canvas, you must use the macro, not call this initializer directly.

## See Also

### Creating an AppKit preview
- [init(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSView)](./init%28_,traits,body%29-158mk.md)
  Creates a preview of an NSView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/preview/init(_:traits:body:)-2viaf)*