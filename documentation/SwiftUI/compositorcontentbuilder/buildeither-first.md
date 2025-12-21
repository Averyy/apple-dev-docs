# buildEither(first:)

**Framework**: SwiftUI  
**Kind**: method

Produces content for a conditional statement in a multi-statement closure when the condition is true.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func buildEither<F>(first: _ConditionalContent<_LimitedAvailabilityCompositorContent, _LimitedAvailabilityCompositorContent>) -> _ConditionalContent<_LimitedAvailabilityCompositorContent, F> where F : CompositorContent
```

#### Discussion

Conditional statements in a [`CompositorContentBuilder`](compositorcontentbuilder.md) must contain both an `if` statement and an `else` statement, and the condition can only perform a compiler check for availability, like in the following code:

```swift
var body: some CompositorContent {
    if #available(visionOS 100, *) {
        MyNewContent()
    } else {
        MyOldContent()
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontentbuilder/buildeither(first:))*