# withCGContext(content:)

**Framework**: SwiftUI  
**Kind**: method

Provides a Core Graphics context that you can use as a proxy to draw into this context.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func withCGContext(content: (CGContext) throws -> Void) rethrows
```

#### Discussion

Use this method to use existing drawing code that relies on Core Graphics primitives.

## Parameters

- `content`: A closure that receives a     that you use to perform drawing operations, just like you draw into a    instance. Any filters, blend mode settings, clip   masks, and other state set before calling    apply to drawing operations in the Core Graphics context as well. Any   state you set on the Core Graphics context is lost when the closure   returns. Accessing the Core Graphics context after the closure   returns produces undefined behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/withcgcontext(content:))*