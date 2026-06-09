# as(_:)

**Framework**: App Intents Testing  
**Kind**: method

Casts the raw value to the specified type.

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
func `as`<T>(_ type: T.Type) throws -> T where T : LosslessStringConvertible
```

#### Discussion

If the raw value isn’t an instance of that type, this method throws an error.

```swift
let enumCase = MyEnumDefinition.makeCase("caseName")

try enumCase.as(String.self) == "caseName"
```

> **Note**: If the raw value cannot be represented as the target type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintentstesting/anyappenum/as(_:))*