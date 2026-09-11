# subscript(dynamicMember:)

**Framework**: App Intents Testing  
**Kind**: subscript

Accesses the return value of the result, without casting.

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
subscript(dynamicMember keyPath: KeyPath<ResolvedIntentResult.ValueKeyPath, Never>) -> (any IntentValueExpressing)? { get }
```

#### Overview

For example:

```swift
let result = try await intent.run()

// Checking for nil.
result.value == nil

// Use it to populate other intents
let intent = PayCoffeeIntent.makeIntent(coffee: result.value)
```

For more information about dynamic-member syntax, see [`dynamicMemberLookup`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes#dynamicMemberLookup) in *[`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/)*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/resolvedintentresult/subscript(dynamicmember:)-7og7e)*