# Preview(_:traits:arguments:body:)

**Framework**: AppKit  
**Kind**: macro

Creates a group of previews of an NSViewController.

**Availability**:
- macOS 27.0+ (Beta)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/preview(_:traits:arguments:body:)-7h191)*