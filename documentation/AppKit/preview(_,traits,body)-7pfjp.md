# Preview(_:traits:body:)

**Framework**: AppKit  
**Kind**: macro  
**Role**: Macro

Preview an NSView.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@freestanding(declaration)
macro Preview(_ name: String? = nil, traits: PreviewTrait<Preview.ViewTraits>..., @PreviewMacroBodyBuilder<NSView> body: @escaping @MainActor () -> NSView)
```

## Parameters

- `name`: Optional display name for the preview, which will appear in the canvas.
- `traits`: Optional list of traits customizing the appearance of the preview.
- `body`: A closure producing an NSView.

## See Also

### Macros
- [var NSIMAGE_UNAVAILABLE_MACCATALYST: Int32](./nsimage_unavailable_maccatalyst.md)
- [var NS_USER_ACTIVITY_SUPPORTED: Int32](./ns_user_activity_supported.md)
- [macro Preview(String?, traits: PreviewTrait<Preview.ViewTraits>..., body: () -> NSViewController)](./preview%28_,traits,body%29-55ljx.md)
  Preview an NSViewController.
- [macro Preview<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> NSView)](./preview%28_,traits,arguments,body%29-5hzef.md)
  Creates a group of previews of an NSView.
- [macro Preview<T>(String?, traits: PreviewTrait<Preview.ViewTraits>..., arguments: [T], body: (T) -> NSViewController)](./preview%28_,traits,arguments,body%29-7h191.md)
  Creates a group of previews of an NSViewController.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/preview(_:traits:body:)-7pfjp)*