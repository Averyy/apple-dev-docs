# objectiveCValue(for:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

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

#### Return Value

`value`, expressed as the Objective-C type defined by [`ObjectiveCValue`](objectivecconvertibleattributedstringkey/objectivecvalue.md).

## Parameters

- `value`: The value to convert.

## See Also

- [static func value(for: Self.ObjectiveCValue) throws -> Self.Value](objectivecconvertibleattributedstringkey/value(for:).md)
  Returns a value of this key’s type for a given Objective-C value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/objectivecconvertibleattributedstringkey/objectivecvalue(for:))*