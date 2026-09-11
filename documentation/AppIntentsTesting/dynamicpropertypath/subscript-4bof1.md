# subscript(_:)

**Framework**: App Intents Testing  
**Kind**: subscript

Accesses a nested property on a collection element by index.

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
subscript(index: Int) -> DynamicPropertyPath { get }
```

#### Overview

The code below shows the syntactic sugar and the equivalent, desugared, subscript syntax.

```swift
let result = try await intent.run() // Expected an array of customer entities

result.value[0].name == nil
CreateCoffeeIntent.makeIntent(customerName: result.value[0].name)
```

For more information about dynamic-member syntax, see [`dynamicMemberLookup`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes#dynamicMemberLookup) in *[`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/)*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypath/subscript(_:)-4bof1)*