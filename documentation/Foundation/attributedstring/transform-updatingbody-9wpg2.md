# transform(updating:body:)

**Framework**: Foundation  
**Kind**: method

Tracks the location of the selection throughout the mutation closure, updating the selection so it represents the same effective locations after the mutation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
mutating func transform<E>(updating selection: inout AttributedTextSelection, body: (inout AttributedString) throws(E) -> Void) throws(E) where E : Error
```

#### Discussion

> **Note**: If the mutation performed does not allow for tracking to succeed (such as replacing the provided inout variable with an entirely different `AttributedString`), the selection is reset to the fallback location at the end of the text.

## Parameters

- `selection`: The selection to track throughout the   closure.
- `body`: A mutating operation, or set of operations, to perform on the   value of  . The value of   is provided to the closure as an    that the closure should mutate directly. Do   not capture the value of   in the provided closure - the closure   should mutate the provided   copy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/transform(updating:body:)-9wpg2)*