# objectiveCValue(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method  
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

`value`, expressed as the Objective-C type defined by [`ObjectiveCValue`](./objectivecvalue.md).

## Parameters

- `value`: The value to convert.

## Default Implementations

### ObjectiveCConvertibleAttributedStringKey Implementations
- [static func objectiveCValue(for: Self.Value) throws -> Self.ObjectiveCValue](./objectivecvalue%28for%29-7whjv.md)
  Returns an Objective-C typed value for a given value of this key’s type.
- [static func objectiveCValue(for: Self.Value) throws -> Self.ObjectiveCValue](./objectivecvalue%28for%29-97cif.md)
  Returns an Objective-C typed value for a given value of this key’s type.

## See Also

### Converting between Swift and Objective-C Types
- [static func value(for: Self.ObjectiveCValue) throws -> Self.Value](./value%28for%29.md)
  Returns a value of this key’s type for a given Objective-C value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/objectivecconvertibleattributedstringkey/objectivecvalue(for:))*