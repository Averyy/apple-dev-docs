# value(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

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

## Return Value

`object`, expressed as this key’s type.

## Parameters

- `object`: The Objective-C value to convert.

## Default Implementations

### ObjectiveCConvertibleAttributedStringKey Implementations
- [static func value(for: Self.ObjectiveCValue) throws -> Self.Value](./value%28for%29-5ggbb.md)
  Returns a value of this key’s type for a given Objective-C value.
- [static func value(for: Self.ObjectiveCValue) throws -> Self.Value](./value%28for%29-5l3da.md)
  Returns a value of this key’s type for a given Objective-C value.

## See Also

### Converting between Swift and Objective-C Types
- [static func objectiveCValue(for: Self.Value) throws -> Self.ObjectiveCValue](./objectivecvalue%28for%29.md)
  Returns an Objective-C typed value for a given value of this key’s type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/objectivecconvertibleattributedstringkey/value(for:))*