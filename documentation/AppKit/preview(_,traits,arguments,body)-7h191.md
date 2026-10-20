# Preview(_:traits:arguments:body:)

**Framework**: AppKit  
**Kind**: macro  
**Role**: Macro

Creates a group of previews of an NSViewController.

**Availability**:
- macOS 27.0+

## Declaration

```swift
@freestanding
(declaration) macro Preview<T>(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], @PreviewBodyBuilder<NSViewController> body: @escaping @MainActor (T) -> NSViewController)
```

## Parameters

- `name`: An optional display name for the preview.
- `traits`: An optional list of traits to customize the preview.
- `arguments`: An array of arguments to pass into `body`.
- `body`: A closure that maps an argument to an NSViewController to preview.

## See Also

### Macros
- [var NSIMAGE_UNAVAILABLE_MACCATALYST: Int32](./nsimage_unavailable_maccatalyst.md)
- [var NS_USER_ACTIVITY_SUPPORTED: Int32](./ns_user_activity_supported.md)
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSViewController)](./preview%28_,traits,body%29-55ljx.md)
  Preview an NSViewController.
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSView)](./preview%28_,traits,body%29-7pfjp.md)
  Preview an NSView.
- [macro Preview<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> NSView)](./preview%28_,traits,arguments,body%29-5hzef.md)
  Creates a group of previews of an NSView.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/preview(_:traits:arguments:body:)-7h191)*