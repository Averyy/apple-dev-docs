# subscript(_:)

**Framework**: App Intents Testing  
**Kind**: subscript

Accesses a collection element by index, without casting.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
subscript(index: Int) -> (any IntentValueExpressing)? { get throws }
```

#### Overview

The code below shows the syntactic sugar and the equivalent, desugared, subscript syntax.

```swift
let result = try await intent.run() // Expected an array as result value

result.value[0] == nil
CreateCoffeeIntent.makeIntent(customerName: result.value[0])
```

For more information about dynamic-member syntax, see [`dynamicMemberLookup`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes#dynamicMemberLookup) in *[`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/)*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/dynamicpropertypath/subscript(_:)-1hj9z)*