# automatic

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The default presentation sizing, appropriate for the platform.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static var automatic: AutomaticPresentationSizing { get }
```

Available when `Self` is `AutomaticPresentationSizing`.

## Discussion

On macOS, `.automatic` resolves to `.form.fitted(horizontal: false, vertical: true)`. On all other platforms, including Mac Catalyst, it resolves to `.form`.

> **See Also**: [`AutomaticPresentationSizing`](../automaticpresentationsizing.md)

## See Also

### Getting built-in presentation size
- [static var fitted: FittedPresentationSizing](./fitted.md)
  The presentation sizing is dictated by the ideal size of the content
- [static var form: FormPresentationSizing](./form.md)
  The size is appropriate for forms and slightly less wide than`.page`
- [static var page: PagePresentationSizing](./page.md)
  The size is roughly the size of a page of paper, appropriate for informational or compositional content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/presentationsizing/automatic)*