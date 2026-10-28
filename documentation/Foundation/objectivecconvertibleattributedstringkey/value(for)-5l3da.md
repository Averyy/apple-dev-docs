# value(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a value of this key’s type for a given Objective-C value.

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
static func value(for object: Self.ObjectiveCValue) throws -> Self.Value
```

Available when `ObjectiveCValue` is `NSNumber`, `Value` conforms to `RawRepresentable`, and `Value.RawValue` is `Int`.

## Return Value

`object`, expressed as this key’s type.

## Parameters

- `object`: The Objective-C value to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/objectivecconvertibleattributedstringkey/value(for:)-5l3da)*