# snippetContentMargins

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The default content margins of the snippet being rendered.

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
var snippetContentMargins: EdgeInsets { get }
```

## Discussion

The value is the same whether or not the snippet applies it: after `EntitySnippetContent/contentMarginsDisabled(_:)`, use it with `padding(_:)` to apply the margins to part of your view. It is zero for snippets that don’t apply content margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/snippetcontentmargins)*