# subscript(dynamicMember:)

**Framework**: App Intents Testing  
**Kind**: subscript

Returns the intent’s output, converted to the inferred type.

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
subscript<T>(dynamicMember keyPath: KeyPath<ResolvedIntentResult.ValueKeyPath, Never>) -> T where T : IntentValueConvertible { get throws }
```

#### Overview

Access the return value using the `value` key path, for example:

```swift
let result = try await intent.run()

// Compare the result with a concrete value.
XCTAssertEqual(try result.value, "Hello World")
```

If the property’s value isn’t an instance of the type `T`, this subscript throws an error.

For more information about dynamic-member syntax, see [`dynamicMemberLookup`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes#dynamicMemberLookup) in *[`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/)*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/resolvedintentresult/subscript(dynamicmember:)-kbqk)*