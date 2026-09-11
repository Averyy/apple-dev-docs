# subscript(dynamicMember:)

**Framework**: App Intents Testing  
**Kind**: subscript

Accesses an intent parameter by name, for comparison with a known value.

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
subscript<T>(dynamicMember identifier: String) -> T where T : IntentValueConvertible { get throws }
```

#### Overview

The code below shows the syntactic sugar and the equivalent, desugared, subscript syntax.

```swift
try intent.someName == "My Name"
try intent[dynamicMember: "someName"] == "My Name"
```

If the property’s value isn’t an instance of the type `T`, this subscript throws an error.

For more information about dynamic-member syntax, see [`dynamicMemberLookup`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes#dynamicMemberLookup) in *[`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/)*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anyappintent/subscript(dynamicmember:)-127ab)*