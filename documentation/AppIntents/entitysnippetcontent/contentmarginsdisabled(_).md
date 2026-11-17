# contentMarginsDisabled(_:)

**Framework**: App Intents  
**Kind**: method  
**Role**: Instance Method

Disables the default content margins.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
func contentMarginsDisabled(_ disabled: Bool = true) -> some EntitySnippetContent<Self.Entity>
```

## Return Value

A snippet that applies the default content margins only if `disabled` is `false`.

## Discussion

By default, the system insets your view from the edges of the snippet by the margins of the container it’s shown in. When you disable them, the snippet draws your view edge to edge, and you’re responsible for any padding. Read `SwiftUICore/EnvironmentValues/snippetContentMargins` with `padding(_:)` to apply the default margins selectively, for example to let an image fill the snippet while its text stays inset.

## Parameters

- `disabled`: Whether to disable the default content margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entitysnippetcontent/contentmarginsdisabled(_:))*