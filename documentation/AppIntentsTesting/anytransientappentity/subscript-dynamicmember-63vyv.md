# subscript(dynamicMember:)

**Framework**: App Intents Testing  
**Kind**: subscript

Accesses a nested entity property by name.

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
subscript(dynamicMember identifier: String) -> DynamicPropertyPath { get }
```

#### Overview

The code below shows the syntactic sugar and the equivalent, desugared, subscript syntax.

```swift
try entity.customer.name == "My Name"
try entity[dynamicMember: "customer"][dynamicMember: "name"] == "My Name"
```

For more information about dynamic-member syntax, see [`dynamicMemberLookup`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes#dynamicMemberLookup) in *[`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/)*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anytransientappentity/subscript(dynamicmember:)-63vyv)*