# objectiveCValue(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an Objective-C typed value for a given value of this key’s type.

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
static func objectiveCValue(for value: Self.Value) throws -> Self.ObjectiveCValue
```

Available when `ObjectiveCValue` is `NSString`, `Value` conforms to `RawRepresentable`, and `Value.RawValue` is `String`.

#### Return Value

`value`, expressed as the Objective-C type defined by [`ObjectiveCValue`](./objectivecvalue.md).

## Parameters

- `value`: The value to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/objectivecconvertibleattributedstringkey/objectivecvalue(for:)-7whjv)*