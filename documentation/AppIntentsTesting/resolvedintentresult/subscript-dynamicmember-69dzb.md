# subscript(dynamicMember:)

**Framework**: App Intents Testing  
**Kind**: subscript

Accesses nested properties of the result’s return value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
subscript(dynamicMember keyPath: KeyPath<ResolvedIntentResult.ValueKeyPath, Never>) -> DynamicPropertyPath { get }
```

#### Overview

For example:

```swift
let result = try await intent.run()

// Accessing properties.
try result.value.customerName == "My Name"
```

For more information about dynamic-member syntax, see [`dynamicMemberLookup`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes#dynamicMemberLookup) in *[`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/)*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/resolvedintentresult/subscript(dynamicmember:)-69dzb)*